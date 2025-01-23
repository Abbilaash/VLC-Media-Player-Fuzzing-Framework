# VLC Media Player Fuzzing Framework

## Overview
This project is a fuzzing framework designed to identify vulnerabilities in VLC Media Player's media parsing and playback functionalities. The framework utilizes Python to generate and test malformed media files against VLC Media Player (version 3.0.16 or later) on Windows, logging crashes and errors encountered during playback.

## Featuring
- **Automated Testing:** Automatically tests a set of malformed media files against VLC Media Player.
- **Crash Detection:** Identifies and logs crashes or unexpected behavior.
- **Detailed Logs:** Identifies and logs crashes or unexpected behavior.

## Project Structure
VLC-Media-Player-Fuzzing-Framework
├── modules
|   ├── samples
|   |   ├── sample_3gp.3gp
|   |   ├── sample_mkv.mkv
|   |   ├── sample_mov.mov
|   |   ├── sample_mp3.mp3
|   |   ├── sample_wmv.wmv
|   |   ├── sample_flv.flv
|   |   ├── test_play.mp4
│   ├── malformed_samples
|   |   ├── sample_3gp_malformed.3gp
|   |   ├── sample_mkv_malformed.mkv
|   |   ├── sample_mov_malformed.mov
|   |   ├── sample_mp3_malformed.mp3
|   |   ├── sample_wmv_malformed.wmv
|   |   ├── sample_flv_malformed.flv
|   |   ├── test_play_malformed.mp4
│   ├── malformed_gen.py   # Generates malformed media files
│   └── crash_log.txt  # Log of crashes and errors encountered
├── README.md          # Project documentation
├── .gitignore         # Ignoring files
└── requirements.txt   # Python dependencies

## Installation
1. Clone repository
   ```git clone https://github.com/Abbilaash/VLC-Media-Player-Fuzzing-Framework.git```
2. Navigate to project directory
   ```cd VLC-Media-Player-Fuzzing-Framework```
3. Run the main file
   ```python main.py```

## Sample Crash Log
```
Crash Log for Malformed Files
============================================================

Testing file: A:\PROJECTS\VLC-Media-Player-Fuzzing-Framework\modules\malformed_samples\sample_3gp_malformed.3gp
============================================================
﻿-- logger module started --
dummy: using the dummy interface module...
avcodec error: Could not open ...
main: end of playlist, exiting
-- logger module stopped --

Testing file: A:\PROJECTS\VLC-Media-Player-Fuzzing-Framework\modules\malformed_samples\sample_mkv_malformed.mkv
============================================================
﻿-- logger module started --
dummy: using the dummy interface module...
mkv error: unknown codec id=`V_MPEG4/�SO/ASP'
...
mkv error: Dummy element too large or misplaced at 1904270... skipping to next upper element
main error: VLC could not identify the audio or video codec
...
-- logger module stopped --
```

## Contributing
Contributions are welcome! If you have suggestions for improvement or have identified issues, please open an issue or submit a pull request.

