import re
import sys

def replace_alamofire_get_data(text):
    # This matches the pattern for get data via AF.request with responseData
    pattern = r'if let url = URL\(string: APIConfigs\.baseURL \+ "(.*?)"\)\{\s*AF\.request\(url, method: \.get\)\.responseData\(completionHandler: \{ response in\s*let status = response\.response\?\.statusCode\s*switch response\.result\{\s*case \.success\(let data\):\s*if let uwStatusCode = status\{\s*switch uwStatusCode\{\s*case 200\.\.\.299:\s*(.*?)\s*break\s*case 400\.\.\.499:\s*print\(data\)\s*break\s*default:\s*print\(data\)\s*break\s*\}\s*\}\s*break\s*case \.failure\(let error\):\s*print\(error\)\s*break\s*\}\s*\}\)\s*\}'
    
    def repl(m):
        endpoint = m.group(1)
        success_code = m.group(2)
        return f"""guard let url = URL(string: APIConfigs.baseURL + "{endpoint}") else {{ return }}
        
        Task {{
            do {{
                let (data, response) = try await URLSession.shared.data(from: url)
                guard let httpResponse = response as? HTTPURLResponse else {{ return }}
                
                switch httpResponse.statusCode {{
                case 200...299:
                    {success_code}
                case 400...499:
                    print("Client error: \(httpResponse.statusCode)")
                default:
                    print("Server error: \(httpResponse.statusCode)")
                }}
            }} catch {{
                print(error)
            }}
        }}"""
    
    return re.sub(pattern, repl, text, flags=re.DOTALL)

def replace_alamofire_get_params(text):
    pattern = r'let parameters = \["name":name\]\s*if let url = URL\(string: APIConfigs\.baseURL\+"(.*?)"\)\{\s*AF\.request\(url, method:\.get,\s*parameters: \["name":name\],\s*encoding: URLEncoding\.queryString\)\s*\.responseData\(completionHandler: \{ response in\s*let status = response\.response\?\.statusCode\s*switch response\.result\{\s*case \.success\(let data\):\s*if let uwStatusCode = status\{\s*switch uwStatusCode\{\s*case 200\.\.\.299:\s*(.*?)\s*break\s*case 400\.\.\.499:\s*print\(data\)\s*break\s*default:\s*print\(data\)\s*break\s*\}\s*\}\s*break\s*case \.failure\(let error\):\s*print\(error\)\s*break\s*\}\s*\}\)\s*\}'

    def repl(m):
        endpoint = m.group(1)
        success_code = m.group(2)
        return f"""guard var urlComponents = URLComponents(string: APIConfigs.baseURL + "{endpoint}") else {{ return }}
        urlComponents.queryItems = [URLQueryItem(name: "name", value: name)]
        guard let url = urlComponents.url else {{ return }}
        
        Task {{
            do {{
                let (data, response) = try await URLSession.shared.data(from: url)
                guard let httpResponse = response as? HTTPURLResponse else {{ return }}
                
                switch httpResponse.statusCode {{
                case 200...299:
                    {success_code}
                case 400...499:
                    print("Client error: \(httpResponse.statusCode)")
                default:
                    print("Server error: \(httpResponse.statusCode)")
                }}
            }} catch {{
                print(error)
            }}
        }}"""
    
    return re.sub(pattern, repl, text, flags=re.DOTALL)

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = replace_alamofire_get_data(content)
    content = replace_alamofire_get_params(content)
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    process_file('lessons/Module_05_Networking_And_Apis.md')
    process_file('lessons/Module_06_Data_Persistence_And_Architecture.md')
    print("Done rewriting AF.request blocks.")
