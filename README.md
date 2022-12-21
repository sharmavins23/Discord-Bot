# Version History for the Pragosh Bot

The following is a printed overview of bot changes and release functionality.

**Current version: [v1.6.3](#version-163)**

# Version 1

## Version 1.0

- Initial creation
- Provides no functionality

_Release date: December 07, 2021_

## Version 1.1

- Adds functionality for 'hello' message
- Adds message embed feature
- Adds auto-reacting to messages containing "Pog" of any case

_Release date: December 08, 2021_

## Version 1.2

- Added beginnings of command functionality
- Changed the bot's bio response from a checked message to a commanded response
- Added auto-replying to messages sent from Tatsu bot
- Added random number generator feature that takes in arguments
- Added help command that provides information for interacting with the bot
- Added coin flip feature

_Release date: December 12, 2021_

### Version 1.2.1

- Fixed auto-replying to Tatsu
- Fixed help command to include coinflip help

_Release date: January 02, 2022_

**Version 1.2.1.1**

- Organized file structure
- Began using Cogs to further increase organization

_Release date: January 02, 2022_

## Version 1.3

- Added background task(s)
- Initializes Spotify Authorization flow
- Initializes Spotify Client Credential flow
- Pulls information from Tribe Blend playlist
- Creates a list for parsed Tribe Blend info
- Edits created list to use Discord role IDs instead of Spotify IDs
- Edits list to only include tracks that are outside of specified date range
- Sends a message to users in list of outdated tracks. Includes check to prevent
  dupe messages

_Release date: January 20, 2022_

## Version 1.4

- Heroku deployment
- Shifting of Git structure to incorporate a development branch and releases
  branch

_Release date: February 14, 2022_

### Version 1.4.1

- Adding necessary pieces to run python script on Heroku

_Release date: February 14, 2022_

**Version 1.4.1.1**

- Editing a few lines, calls, and imports.

_Release date: February 16, 2022_

### Version 1.4.2

- Changing spotify passive workflow to use client credential flow as opposed to
  client authorization code flow
- `.gitignore` file expanded to include locally saved files that are used for
  development testing

_Release date: February 16, 2022_

**Version 1.4.2.1**

- Attempt at resolving issue with sending messages

_Release date: February 16, 2022_

**Version 1.4.2.2**

- Resolving issue with sending messages

_Release date: February 16, 2022_

**Version 1.4.2.3**

- Hotfix to resolve crashing of web service on Heroku

_Release date: February 16, 2022_

## Version 1.5

- Completely redoing Spotify implementation for the server
- Added this README and other little stuff for nice-ness
- Merged in collaborator changes for RNG command
- Cleaned up token/ID retrieval and handling

_Release date: May 1, 2022_

### Version 1.5.1

- Using Authorization Code Workflow to update playlist

_Release date: May 1, 2022_

**Version 1.5.1.1**

- Edited environment vars to enable AC flow to work on deployed Heroku app

_Release date: May 2, 2022_

### Version 1.5.2

- Splitting Spotify work into several files/functions

_Release date: May 4, 2022_

### Version 1.5.3

- Spotify update command is functional
- Changed person data dictionary in tokens file

_Release date: June 28, 2022_

### Version 1.5.4

- Adjusting random song selection to compensate for various playlist sizes
- Better fool-proofed the random number command to be resilient to bad inputs
- Changed random color command to reply with an embed and image

_Release date: June 30, 2022_

### Version 1.5.5

- Adding feature to count the artists in a playlist
- Used feature to return the top 5 artists in a playlist

_Release date: July 21, 2022_

**Version 1.5.5.1**

- Modifying help command for topartists command

_Release date: July 21, 2022_

### Version 1.5.6

- Correctly implementing Spotify OAuth to function on Heroku
- Changed update of Tribe Blend 2.0 to every 24 hours
- Removed notification of Tribe Blend 2.0 updating

_Release date: August 1, 2022_

## Version 1.6

- Implemented a DB to hold values not important enough to be a config var
- Updated Spotipy custom cache handler to replace config var usage with DB
  requests
- Updated Spotify logic for updateTB2 to compensate for users with 1 playlist
- Correctly implemented Spotify auth token checks to use records in DB
- Implemented update of DB Spotify auth token when token is refreshed
- Implemented record keeping of updates to TB 2.0 playlist
- Updated spotifypassives logic to check DB records of playlist updates

_Release date: August 11, 2022_

### Version 1.6.1

- Created second cache handler so we have separate tokens for CC vs CAC flows
- Added cache handler to client credentials flow

_Release date: August 14, 2022_

### Version 1.6.2

- Implemented saving the TB 2.0 results to a DB table
- Implemented checkpoint annotations command for TB 2.0
- Altered the conditional logic for passively updating TB 2.0
- Added another instant reply (Radical Islam)
- Implemented song annotation command for TB 2.0

_Release date: November 22, 2022_

### Version 1.6.3

- Revamped random number once again. Added more edge case control
  - Check for single number given
  - Added limit check for count
- Changed coin flip to send actual file
- Throughly commented randomness.py

_Release date: December 21, 2021_
