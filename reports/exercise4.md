# Bug reports for exercise4.py

Line: 3  
Problem: Hardcoded default password "admin123" is used if ADMIN_PASSWORD is not set in environment, violating security best practices.  
Example: If ADMIN_PASSWORD is not set, the application uses a hardcoded password, making it vulnerable to brute-force attacks.  
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD") or "admin123"

Line: 8  
Problem: The function returns `True` if the password is not empty and matches the admin password, but if `ADMIN_PASSWORD` is empty, it will incorrectly return `True` for any password due to the `!= ""` check.  
Example: If ADMIN_PASSWORD is empty, `check_admin("any")` returns `True`, which is a security vulnerability.  
Fix: return ADMIN_PASSWORD == password

Line: 13  
Problem: The SQL query uses f-string formatting (implied via `?` placeholder) but the parameter is correctly passed; however, the use of `?` is correct and safe. No vulnerability.  
Example: No SQL injection risk due to proper parameterization.  
Fix: (No fix needed)  

Note: Line 13 is safe and correctly uses parameterized query. No bug.  
Final output only includes actual issues:

Line: 3  
Problem: Hardcoded default password "admin123" is used if ADMIN_PASSWORD is not set in environment, violating security best practices.  
Example: If ADMIN_PASSWORD is not set, the application uses a hardcoded password, making it vulnerable to brute-force attacks.  
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD") or "admin123"

Line: 8  
Problem: The function returns `True` if the password is not empty and matches the admin password, but if `ADMIN_PASSWORD` is empty, it will incorrectly return `True` for any password due to the `!= ""` check.  
Example: If ADMIN_PASSWORD is empty, `check_admin("any")` returns `True`, which is a security vulnerability.  
Fix: return ADMIN_PASSWORD == password
