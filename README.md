# TheFarmerWasReplaced
Code repo for all files related to The Farmer was Replaced

Figuring out how to do this was really annoying because under linux finding the wine file system isn't always easy.
For me, I had the game installed on a fstab mounted location, and I think that caused wine to store the save data in a location other than the steam install path.
It may also just be the expected behaviour that the save data is stored alongside the game install path, I wasn't able to find any information about this anywhere online, all clues pointed to the steam install dir. Though I did also seem to have stale save data under the install dir (`~/.steam/steam/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/`)

Anyway, here's how I did this:

1) Find the wine directory for the game save data, mine was located under:
`/mnt/Games/SteamLibrary/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/`

2) Copy all of the .py files that are already there into your repo dir:
`cp /path/to/saves/*.py /path/to/repo`

3) Symlink all of the .py files from your repo into the save file location:
`ln -s /path/to/repo/*.py /path/to/saves/`
Note: Doing this the other way around (save dir to repo) doesn't work because of the way that git treats symlinks
Also, sym links should always use absolute paths for the source file. The destination can be relative.

4) Do git things as per normal.

Keep in mind, any time you make a new file in the repo dir you'll need to also symlink it into the game save dir.

I'm keeping this handy one liner for when I need to do this in future:

`ln -s /home/blackout/Documents/code/TheFarmerWasReplaced/Save0/*.py /mnt/Games/SteamLibrary/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/Saves/Save0/`