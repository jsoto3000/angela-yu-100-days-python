# Angela Yu - Python Day 24
## How to Open, Read, and Write to Files in Python

- File System
  - Open and Read
  - Open and Write
    - "mode" keyword to set file as writable
    - 'a' for append
- "with" keyword will manage open and closing of files
- see main.py for examples

## Understanding Relative and Absolute File Paths

- File Path:
  - / Root Directory or Folder &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp; &nbsp;/
    - Work Folder &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp; &emsp; &emsp; &emsp; &nbsp;/Work/ 
      - report.doc file (inside Work Folder) &emsp; &emsp; &emsp;&nbsp; &nbsp; /Work/report.doc
        - Project Folder &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &nbsp; &nbsp; &nbsp; /Work/Project/
          - talk.ppt file (inside Project Folder) &emsp; /Work/Project/talk.ppt
- Absolute File Path
  - Always starts relative to the Root directory/folder
  - starts from the origin
  - it is the full path to location of a file
  - i.e., /Work/Project/talk.ppt
- Absolute Path
  - Starts relative to the current working directory/folder
  - i.e., current working directory is /Work/Project/
  - relative path for talk.ppt file is ./talk.ppt
  - "." signifies look in the current directory for file
  - ".." signifies go one step up to the above parent directory/folder 
    - ../report.doc (again current working directory is /Work/Project/)