import os, zipfile, tempfile, shutil, glob, re

DOWNLOADS_DIR = "/Users/nsm/cs4520/downloads"

def read_file(p):
    with open(p, "r", encoding="utf-8") as f: return f.read()

def write_file(p, c):
    with open(p, "w", encoding="utf-8") as f: f.write(c)

def process_toml(p):
    c = read_file(p)
    c = c.replace('"8.5.0"', '"8.8.0"')
    c = c.replace('"2.0.21"', '"2.1.0"')
    write_file(p, c)

def process_app_build_gradle(p, is_topic_4_plus, is_topic_11_plus):
    c = read_file(p)
    
    # KAPT to KSP
    c = re.sub(r'id\("kotlin-kapt"\)', 'id("com.google.devtools.ksp")', c)
    c = re.sub(r'kapt\(', 'ksp(', c)

    if is_topic_4_plus:
        # Inject serialization plugin if missing
        if "plugin.serialization" not in c:
            c = re.sub(r'(plugins\s*\{)', r'\1\n    id("org.jetbrains.kotlin.plugin.serialization") version "2.1.0"', c)
        
        # Inject kotlinx-serialization-json dependency
        if "kotlinx-serialization-json" not in c:
            c = re.sub(r'(dependencies\s*\{)', r'\1\n    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.1")', c)
            
        # Ensure navigation-compose is 2.8.0 or higher
        c = re.sub(r'androidx\.navigation:navigation-compose:2\.[0-7]\.\d+', 'androidx.navigation:navigation-compose:2.8.0', c)

    if is_topic_11_plus:
        # Remove accompanist
        c = re.sub(r'implementation\("com\.google\.accompanist:accompanist-permissions.*?\n', '', c)

    write_file(p, c)

def replace_in_kt(base_dir, topic_num):
    for root, _, files in os.walk(base_dir):
        for f in files:
            if not f.endswith(".kt"): continue
            p = os.path.join(root, f)
            c = read_file(p)
            changed = False
            
            if topic_num >= 4:
                # Replace Routes.HOME -> Home(), etc.
                if "Routes." in c:
                    c = c.replace('Routes.HOME', 'Home')
                    c = c.replace('Routes.SEARCH', 'Search')
                    c = c.replace('Routes.SAVED', 'Saved')
                    c = c.replace('Routes.MAP', 'Map')
                    c = c.replace('Routes.CAMERA', 'Camera')
                    c = c.replace('Routes.SETTINGS', 'Settings')
                    
                    # Update NavHost composable strings -> types
                    c = re.sub(r'composable\(Home\)', 'composable<Home>', c)
                    c = re.sub(r'composable\(Search\)', 'composable<Search>', c)
                    c = re.sub(r'composable\(Saved\)', 'composable<Saved>', c)
                    c = re.sub(r'composable\(Map\)', 'composable<Map>', c)
                    c = re.sub(r'composable\(Camera\)', 'composable<Camera>', c)
                    c = re.sub(r'composable\(Settings\)', 'composable<Settings>', c)
                    
                    # Replace popBackStack(Routes.HOME, -> popBackStack<Home>(
                    c = re.sub(r'popBackStack\(Home,', 'popBackStack<Home>(', c)
                    c = re.sub(r'popBackStack\(Search,', 'popBackStack<Search>(', c)
                    c = re.sub(r'popBackStack\(Saved,', 'popBackStack<Saved>(', c)
                    
                    # Replace getBackStackEntry
                    c = re.sub(r'getBackStackEntry\(Home\)', 'getBackStackEntry<Home>()', c)
                    
                    # Replace DETAIL route entirely
                    c = re.sub(r'composable\(\s*route\s*=\s*Routes\.DETAIL,\s*arguments\s*=\s*listOf\(navArgument\("city"\)\s*\{\s*type\s*=\s*NavType\.StringType\s*\}\),\s*\)\s*\{\s*entry\s*->\s*val\s*city\s*=\s*entry\.arguments\?\.getString\("city"\)\s*\?\:\s*return@composable', 
                               r'composable<Detail> { entry ->\n            val city = entry.toRoute<Detail>().city', c)

                    # Update navController.navigate(Routes.DETAIL + "/${city.name}") to navController.navigate(Detail(city.name))
                    # Actually, it's usually: navController.navigate(Routes.DETAIL + "/${city.name}")
                    c = re.sub(r'navController\.navigate\(Routes\.DETAIL \+ "/\$\{([^}]+)\}"\)', r'navController.navigate(Detail(\1))', c)
                    # or navController.navigate("detail/${city.name}")
                    c = re.sub(r'navController\.navigate\("detail/\$\{([^}]+)\}"\)', r'navController.navigate(Detail(\1))', c)
                    
                    changed = True
                    
                # Add kotlinx.serialization imports if missing
                if "import kotlinx.serialization.Serializable" not in c and "composable<" in c:
                    c = "import kotlinx.serialization.Serializable\nimport androidx.navigation.toRoute\n" + c
                    changed = True

            if topic_num >= 11:
                if "rememberPermissionState" in c:
                    # Very targeted replacement for LocationWeatherButton or LocationPermissionWrapper
                    # Since it's hard to parse AST, we can just replace the Accompanist import
                    c = c.replace('import com.google.accompanist.permissions.rememberPermissionState', '')
                    c = c.replace('import com.google.accompanist.permissions.isGranted', '')
                    c = c.replace('import com.google.accompanist.permissions.shouldShowRationale', '')
                    
                    c = re.sub(r'val permState = rememberPermissionState\(Manifest.permission.ACCESS_COARSE_LOCATION\).*?when \{.*?permState\.status\.isGranted ->\s*(.*?)\s*permState\.status\.shouldShowRationale ->\s*(.*?)\s*else ->\s*(.*?)\s*\}',
                        r'''var hasPermission by remember { mutableStateOf(ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED) }
    val permissionLauncher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { hasPermission = it }

    if (hasPermission) { \1 } else { \2
        // Also handle else block here logically, or combine.
    }''', c, flags=re.DOTALL)
                    
                    changed = True
            
            if changed: write_file(p, c)
            
        # Delete Routes.kt and create Destinations.kt
        for f in files:
            if f == "Routes.kt":
                p = os.path.join(root, f)
                os.remove(p)
                dest_p = os.path.join(root, "Destinations.kt")
                dest_c = """package com.example.skycast.ui.navigation
import kotlinx.serialization.Serializable

@Serializable object Home
@Serializable object Search
@Serializable object Saved
@Serializable object Map
@Serializable object Camera
@Serializable object Settings
@Serializable data class Detail(val city: String)
"""
                write_file(dest_p, dest_c)


def process_zip(zip_path):
    m = re.search(r'topic_(\d+)', zip_path)
    topic_num = int(m.group(1)) if m else 0

    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(tmp)
            
        # Process files
        for root, _, files in os.walk(tmp):
            for f in files:
                p = os.path.join(root, f)
                if f == "libs.versions.toml":
                    process_toml(p)
                elif f == "build.gradle.kts" and "app" in root:
                    process_app_build_gradle(p, topic_num >= 4, topic_num >= 11)
                    
        replace_in_kt(tmp, topic_num)

        # Repackage
        temp_zip = zip_path + ".tmp"
        with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(tmp):
                for f in files:
                    file_path = os.path.join(root, f)
                    arcname = os.path.relpath(file_path, tmp)
                    zf.write(file_path, arcname)
                    
        os.replace(temp_zip, zip_path)

for z in glob.glob(os.path.join(DOWNLOADS_DIR, "*.zip")):
    print("Processing", z)
    process_zip(z)

