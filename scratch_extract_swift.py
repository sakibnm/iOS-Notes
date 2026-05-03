import re
import sys

def extract_swift_blocks(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    blocks = re.findall(r'```swift\n(.*?)\n```', content, re.DOTALL)
    print(f"File: {filename}")
    for i, block in enumerate(blocks):
        print(f"--- Block {i+1} ---")
        print(block)
        print("------------------\n")

if __name__ == '__main__':
    extract_swift_blocks('lessons/Module_01_Getting_Started.md')
    print("====================================")
    extract_swift_blocks('lessons/Module_02_Swift_Fundamentals.md')
