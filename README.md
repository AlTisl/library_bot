[На русском](README_ru.md)  
[Українською](README_ua.md)

# library_bot
This is a Telegram bot for the library of National university Zaporizhzhia Polytechnic. It provides users with access to the library's online services (literature search, request processing, etc.), contains publication formatting guidelines, and other useful materials.

## Realization
This bot was written in Python using the aiogram 3.20.0 library.  
Redis is used for storing states and the FileIDs of uploaded objects.

### Files and directories
- requirements.txt - project dependencies list;
- main.py - application start point;
- config_reader.py - contains the Settings class, which reads the bot token and Redis connection parameters from an .env file;
- database.py - this file contains functions for writing to and reading from a Redis storage static files' FileID values;
- media_sending.py - functions for static files (images, animations, documents) sending by using FileID (if exists) or by using file upload;
- decorators.py - contains a decorator for functions from the media_sending module; it checks whether the uploaded object's FileID exists in the storage and, depending on the result, passes either the file object or its FileID to wrapped function;
- keyboards.py - keyboards and inline buttons;
- strings.py - message texts stored as Text class objects;
- handlers/ - commands handlers;
- constants/ - constants used in the project: paths to static files, button labels, and URLs for inline buttons;
- resources/ - static files used in project.