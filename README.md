## ppsspp_upscale_utils
Facilitates workflow organization for PPSSPP upscale projects.
* Organize large groups of files with drag-and-drop simplicity
* Generate textures.ini file for your project

### Prerequisites
* Python 3.7

## Step 1: PPSSPP Configuration
1. Open PPSSPP Settings Menu:
```Settings > Tools > Developer Tools```
2. Check 'Save New Textures'
3. Click 'Create/Open textures.ini file for current game.'<br/>
  > Make note of this location! ```[PPSSPP DIRECTORY]/TEXTURES/[PSP GAME ID]``` <br/>
  _This is your **[GID] directory (Game ID).**_ 
## Step 2: Prepare Directories
1. Copy ```generate_folders.py``` and ```generate_texture_list.py``` to ```[GID]/new```
> PPSSPP will save ```[GID]/new``` if they are not yet listed in the ```textures.ini``` file!
2. Run ```generate_folders.py```
> You can add multiple 'root' directories' Note: This script is designed to create directory trees three directories deep. <br/>
> This script will also create temporary ```sorting folders``` for textures which have a more generalized use.
* Think carefully on how you organize your project. You may end up having _thousands_ of files!
* It is _**highly recommended**_ that you organize your project by ```in-game location```!<br/>

Take note of the new directories in ```[GID]/new```
## Step 3: Create Symbolic Links in Windows (optional)
> _Symbolic links_ (also known as ```"symlinks"```) are essentially 'shortcuts' which point your operating system to another file or folder at a different storage location.
> ```Symlinks``` may be used to optimize your workflow without creating redundant copies of files. </br>
> * In Windows Vista/7/10, users can create linked directories or ```"junctions"``` using the following commandline instruction: <br>
>  ```mklink /J "[target directory]" "[source directory]"```
1. Press the ```windows key``` or ```start button``` and type ```'cmd'``` to search for the ```Command Line``` utility.
2. ```Right click``` on ```Command Line``` and select ```Run as administrator```.
3. Navigate to ```[GID]```by entering ```cd [path to GID]``` <br/>
_Hint: You can copy the ```directory path``` using ```File Explorer```._
4. Create ```junction``` for the ```textures``` directory.
> Example: ```mklink /J "[_FULL PATH_ to GID]/textures/" "[_FULL PATH_ to GID]/new/textures/"``` <br/>
> _Using a symlink in this way will make it easier for your to keep everything in the ```/new/``` directory while you are still working. Whenever you are ready to release your texture pack, users will be able to simply place the pack in ```[GID]``` without any modifications._
5. Create ```symlink``` for ```textures.ini```: <br/>
```mklink "[_FULL PATH_ to GID]/new/textures.ini" "[_FULL PATH_ to GID]/textures.ini"```
> Note that this command is not a Junction. Do not include ```"/J"```!
6. Create ```junctions``` in ```sorting``` folder:
Similar to ```#4```, create ```junctions``` for each of the temporary ```sorting folders``` created in ```Step 2: Preparing Directories```.</br>
This time, create your shortcuts in the ```sorting`` folder in ```[GID]/new```.

## Generating textures.ini file with ```generate_texture_list.py```.
Set up your workflow such that you have three windows open, one each for the following directories:
> ```[GID]/new/```, ```[GID]/sorting/```, and ```[GID]/textures/```.

1. Simply play through an area of the game with the textures you want to replace. PPSSPP will save the textures in ```[GID]/new/```.
2. Create a ```save state```, then _fully exit_ the game to PPSSPP's ```main menu```.
> _PPSSPP will not reload textures.ini if you do not fully exit the emulation._
3. Select any general, repeated, or non-area-specific textures in the ```/new/``` directory and move them into their appropriate ```sorting folders```.
4. Leave any textures specific to your targeted ```in-game area``` in ```/new/```.
5. In your ```[GID]/textures/``` window, navigate to the directory containing the ```subdirectory``` which corresponds to your ```in-game area```.
> _Note: You can create directories yourself if you overlooked a certain area or feel you want to change your structure._
6. Drag the ```in-game area``` directory onto ```generate_texture_list.py```
7. ```Resume``` game emulation and ```load state```.
8. Repeat previous steps with the ```next area```.


