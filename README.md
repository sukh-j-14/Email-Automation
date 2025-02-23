# 📧 Email Automation  

## 🚀 Overview  
This project automates sending **certificates or custom documents** to multiple recipients using Python. It streamlines **bulk email distribution with attachments**, reducing manual effort. **Google Mail authentication** ensures secure access.  

🔹 Ideal for **event organizers, educators, and businesses** needing **efficient, scalable email automation**.  

## 📌 Steps to Use  

### 1️⃣ Prepare the Recipients List  
- In `recipients.xlsx`, collect **names and emails** from a Google Form or any source of your choice.  

### 2️⃣ Bulk Create Certificates  
- Use **Bulk Create** in **Canva** to generate certificates in bulk by passing the relevant column from `recipients.xlsx`.  

### 3️⃣ Naming Sequence  
- Ensure certificates follow a **natural number sequence**: `1,2,3,...,n`.  

### 4️⃣ Organizing Certificates  
- Store certificates in the **Certificate File** folder.  
- Name each file according to the **natural number sequence** (`1,2,3,...,n`).  

### 5️⃣ Generate an App Password  
- Visit **[Google App Passwords](https://myaccount.google.com/apppasswords)**.  
- In the **App Name**, type `"Mail"` and generate a **password** for authentication.  

### 6️⃣ Configure `send_certificates.py`  
- Open `send_certificates.py` and enter:  
  - **Your Gmail address**  
  - **Generated app password**  
- Customize the email content in the `set_content` section.  

### 7️⃣ Run the Script  
- Execute the script to **send emails with attachments** automatically! 🎉  

## ⚠️ Disclaimer  
🚫 **For educational purposes only.** Do not use for **spamming** or unsolicited emails.  

---

📩 **Automate your email workflow efficiently!**  
