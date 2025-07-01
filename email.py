import re

def extract_emails():
    input_file = input("Enter input text file path: ")
    output_file = input("Enter output file path for emails: ")
    
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        
        emails = re.findall(email_pattern, text)
        unique_emails = list(set(emails))  
        
       
        with open(output_file, 'w', encoding='utf-8') as f:
            for email in unique_emails:
                f.write(email + '\n')
        
        print(f"Found {len(unique_emails)} unique email addresses.")
        print(f"Saved to: {output_file}")
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    extract_emails()
