# SSRF Vulnerability Labs

This repository contains a series of labs demonstrating SSRF (Server-Side Request Forgery) vulnerabilities, showcasing how attackers can exploit poorly implemented features to access internal services. These labs are designed to demonstrate common security mistakes and provide insights into how to secure web applications.

## Labs Overview:

### Lab 1: Basic SSRF
- **Vulnerability:** SSRF vulnerability in fetching URLs from user input.
- **Issue in Code:** 
  - In `Lab 1`, the application takes user input in the form of a URL and fetches content from the provided URL without validating whether it points to an internal or external resource.
  - The lack of validation makes it possible for an attacker to submit URLs that target sensitive internal resources, such as internal APIs or local files.

- **Impact:** 
  - An attacker can submit internal URLs (e.g., `http://127.0.0.1:5000/secret`) and access sensitive information that should not be exposed to the public, effectively bypassing the application’s intended security boundaries.
  
- **How to Fix:**
  - Validate the URL to ensure that only external resources are accessed.
  - Implement a whitelist of trusted external domains or IP addresses.
  - Avoid using user input directly in network requests.
  
---

### Lab 2: Internal API Access via SSRF
- **Vulnerability:** SSRF vulnerability allowing access to internal API endpoints.
- **Issue in Code:**
  - In `Lab 2`, the code does not properly filter or validate the input URL, allowing attackers to target internal endpoints (e.g., `/internal-api`).
  - The user is able to submit any URL (including `localhost` or `127.0.0.1`), allowing them to access internal APIs or other sensitive services that are meant to be private.

- **Impact:**
  - Attackers can probe and gain access to internal systems, APIs, or databases that are not publicly accessible.
  - This could lead to data leaks, unauthorized actions, or further attacks like lateral movement within a network.

- **How to Fix:**
  - Implement domain or IP whitelisting to restrict which internal services can be accessed.
  - Introduce input validation and filtering to block requests that attempt to access local services or internal APIs.
  - Use a proxy server or other intermediary that can block access to internal services.
  
---

### Lab 3: SSRF via URL Redirection
- **Vulnerability:** SSRF via URL redirection to internal services.
- **Issue in Code:**
  - In `Lab 3`, the application follows HTTP redirects (e.g., 302 redirects) without validating whether the destination URL is external or internal.
  - By crafting a redirect URL (`http://example.com/redirect?to=http://127.0.0.1:5000/internal-secret`), attackers can cause the application to follow the redirect to an internal endpoint, potentially exposing sensitive data.

- **Impact:**
  - The ability to follow redirects allows attackers to target internal resources, even if direct access is blocked by firewalls or other security measures.
  - This could result in the exposure of sensitive internal pages, APIs, or data.

- **How to Fix:**
  - Block or restrict following redirects to URLs pointing to internal addresses.
  - Implement a validation layer for the `Location` header in HTTP responses to prevent unauthorized redirections.
  - Ensure that redirects only occur to trusted, external URLs by validating the `to` parameter in URL redirects.

---

## How the Application Works:

1. **Lab 1: Basic SSRF**
   - The user enters a URL into a form. The app fetches content from the provided URL and displays it.
   - **Vulnerability:** No validation is performed on the entered URL, allowing an attacker to request internal URLs.

2. **Lab 2: Internal API Access**
   - The user enters a URL into a form, and the app fetches content from that URL.
   - **Vulnerability:** Attackers can use this feature to request internal API URLs (e.g., `http://127.0.0.1:5000/internal-api`), bypassing the security of internal systems.

3. **Lab 3: SSRF via Redirect**
   - The app follows redirects from one URL to another.
   - **Vulnerability:** An attacker can force the app to follow redirects to internal services by providing malicious `to` URL parameters.

---

## Setup

1. Clone the repository:

   ```bash
   git clone git@github.com:Yuvaraj-019/SSRF-Server-Side-Request-Forgery.git
or http
git clone https://github.com/Yuvaraj-019/SSRF-Server-Side-Request-Forgery.git

   cd ssrf-labs
