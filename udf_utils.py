# Disclaimer:
# These functions are tailored specifically for parsing structured job bulletin text files
# that follow a consistent format (e.g., POSITION, CLASS CODE, ANNUAL SALARY, etc.).
# If used with files of different structures or formats, modifications to the regex
# patterns and logic may be required to ensure accurate parsing.
# Please check the structure of the text file shared.
# -------------------------------------------------------------------------------------------

import re
from datetime import datetime


# Extract the file name from the content
def extract_file_name(content):
    """
    Extracts the file name from the given file content.
    """
    try:
        content = content.strip()
        return content.split('\n')[0]
    except Exception as e:
        raise ValueError(f"Error extracting file name: {str(e)}")


# Extract the position from the content
def extract_position(content):
    """
    Extracts the position name from the file content.
    """
    try:
        content = content.strip()
        return content.split('\n')[0]
    except Exception as e:
        raise ValueError(f"Error extracting position: {str(e)}")


# Extract the class code from the content
def extract_class_code(content):
    """
    Extracts the class code from the content using regex.
    """
    try:
        match = re.search(r'(Class Code:)\s+(\d+)', content)
        return match.group(2) if match else None
    except Exception as e:
        raise ValueError(f"Error extracting class code: {str(e)}")


# Extract the start date from the content
def extract_start_date(content):
    """
    Extracts the start date from the file content.
    """
    try:
        match = re.search(r'(Open [Dd]ate:)\s+(\d{2}-\d{2}-\d{2})', content)
        return datetime.strptime(match.group(2), '%m-%d-%y') if match else None
    except Exception as e:
        raise ValueError(f"Error extracting start date: {str(e)}")


# Extract the end date from the content
def extract_end_date(content):
    """
    Extracts the end date using regex with month and year patterns.
    """
    try:
        match = re.search(
            r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s(\d{1,2}, \d{4})',
            content,
        )
        return datetime.strptime(match.group(0), '%B %d, %Y') if match else None
    except Exception as e:
        raise ValueError(f"Error extracting end date: {str(e)}")


# Extract salary range
def extract_salary(content):
    """
    Extracts the salary range (start and end) from the content.
    """
    try:
        salary_pattern = r'\$(\d{1,3}(?:,\d{3})+).*to.*\$(\d{1,3}(?:,\d{3})+)'
        match = re.search(salary_pattern, content)
        if match:
            salary_start = float(match.group(1).replace(',', ''))
            salary_end = float(match.group(2).replace(',', ''))
            return salary_start, salary_end
        else:
            return None, None
    except Exception as e:
        raise ValueError(f"Error extracting salary: {str(e)}")


# Extract job requirements
def extract_requirements(content):
    """
    Extracts the job requirements section from the content.
    """
    try:
        match = re.search(r'REQUIREMENTS?/\s?MINIMUM_QUALIFICATIONS?(.*?)(PROCESS NOTES?)', content, re.DOTALL)
        return match.group(1).strip() if match else None
    except Exception as e:
        raise ValueError(f"Error extracting requirements: {str(e)}")


# Extract notes from the content
def extract_notes(content):
    """
    Extracts the notes section from the content.
    """
    try:
        match = re.search(r'NOTES?:\s*(.*?)(?=\bDUTIES?:)', content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else None
    except Exception as e:
        raise ValueError(f"Error extracting notes: {str(e)}")


# Extract job duties
def extract_duties(content):
    """
    Extracts the duties section from the content.
    """
    try:
        match = re.search(r'DUTIES:\s*(.*?)(?=\bREQ[A-Z]|\bNOTES?:)', content, re.DOTALL)
        return match.group(1).strip() if match else None
    except Exception as e:
        raise ValueError(f"Error extracting duties: {str(e)}")


# Extract selection process
def extract_selection(content):
    """
    Extracts selection details using regex.
    """
    try:
        matches = re.findall(r'[A-Z][a-z]+(\s\.\s)+', content)
        return [match.strip() for match in matches] if matches else None
    except Exception as e:
        raise ValueError(f"Error extracting selection process: {str(e)}")


# Extract experience length
def extract_experience_length(content):
    """
    Extracts experience length from the content.
    """
    try:
        match = re.search(r'(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)\s(years?)\s(of\sfull-time)', content)
        return match.group(1) if match else None
    except Exception as e:
        raise ValueError(f"Error extracting experience length: {str(e)}")


# Extract education length
def extract_education_length(content):
    """
    Extracts the education length from the content.
    """
    try:
        match = re.search(
            r'(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)\s(years?)\s(college|university)',
            content,
        )
        return match.group(1) if match else None
    except Exception as e:
        raise ValueError(f"Error extracting education length: {str(e)}")


# Extract application location
def extract_application_location(content):
    """
    Determines whether the application is accepted online or otherwise.
    """
    try:
        match = re.search(r'Applications? will only be accepted on-?line', content, re.IGNORECASE)
        return 'Online' if match else 'Mail or In Person'
    except Exception as e:
        raise ValueError(f"Error extracting application location: {str(e)}")
