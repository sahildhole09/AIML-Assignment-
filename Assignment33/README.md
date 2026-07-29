# Duplicate File Removal Automation

## Project Description

Duplicate File Removal Automation is a Python automation project that periodically scans a specified directory, detects duplicate files using the MD5 checksum algorithm, removes duplicate copies while keeping one original file, generates a detailed log file, and sends the log file to the specified email address.

---

## Features

- Recursive directory scanning
- MD5 checksum-based duplicate detection
- Automatic duplicate file deletion
- Keeps one original copy
- Timestamp-based log generation
- Creates Marvellous folder automatically
- Email notification with log attachment
- Periodic execution
- Exception handling
- Modular programming
- Command-line arguments
- Help and Usage options

---

## Requirements

### Software

- Python 3.10 or above
- Windows/Linux

### Python Libraries

- os
- sys
- hashlib
- datetime
- time
- re
- smtplib
- email

### Other Requirements

- Internet connection
- Gmail account
- Gmail App Password

---

## Project Structure

```
DuplicateFileRemovalProject/

│
├── DuplicateFileRemoval.py
├── DuplicateModule.py
├── LogModule.py
├── MailModule.py
├── README.md
│
└── Marvellous/
      DuplicateRemovalLog_Date_Time.log
```

---

## Command Line Arguments

| Argument | Description |
|----------|-------------|
| DirectoryPath | Absolute path of directory |
| Interval | Time interval in minutes |
| ReceiverEmail | Receiver email address |

---

## Execution Command

```bash
python DuplicateFileRemoval.py "D:\Demo" 30 receiver@gmail.com
```

---

## Help Command

```bash
python DuplicateFileRemoval.py --help
```

or

```bash
python DuplicateFileRemoval.py -h
```

---

## Usage Command

```bash
python DuplicateFileRemoval.py --usage
```

or

```bash
python DuplicateFileRemoval.py -u
```

---

## Log File

The project automatically creates a folder named

```
Marvellous
```

Inside this folder a log file is generated.

Example

```
DuplicateRemovalLog_28_07_2026_19_45_30.log
```

The log file contains

- Starting time
- Completion time
- Directory scanned
- Total files scanned
- Duplicate files found
- Duplicate files deleted
- Deleted file paths
- MD5 checksum
- Email status

---

## Email Configuration

The project uses Gmail SMTP Server.

Replace

```python
SenderEmail = "yourgmail@gmail.com"

AppPassword = "your_16_character_app_password"
```

with your own Gmail credentials.

Never use your normal Gmail password.

Always use a Gmail App Password.

---

## Working

1. Read command-line arguments.
2. Validate directory.
3. Validate email.
4. Validate interval.
5. Scan directory recursively.
6. Calculate MD5 checksum.
7. Detect duplicate files.
8. Delete duplicate copies.
9. Generate log file.
10. Send log through email.
11. Wait for the given interval.
12. Repeat the process.

---

## Sample Output

```
Duplicate File Removal Automation Started...

Scanning Directory...

Duplicate Files Deleted : 12

Log File Created Successfully

Email Sent Successfully

Waiting for 30 minutes...
```

---

## Advantages

- Saves storage space
- Fast duplicate detection
- Automatic execution
- Generates detailed report
- Easy to maintain
- Modular design
- Suitable for large folders

---

## Important Notes

- Deleted files cannot be recovered.
- Test the project on a sample folder first.
- Do not hard-code Gmail passwords.
- Keep one original file from every duplicate group.
- Duplicate files are identified using checksum values, not filenames.

---

## Author

Name : Sahil Ashok Dhole

Course : Python Automation & Machine Learning

Project : Duplicate File Removal Automation