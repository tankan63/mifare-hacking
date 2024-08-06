# mifare-hacking
Docker stuff for hacking mifare classic cards, this is mostly used for conferences and demos.
DEFCON - August 2023, Las Vegas, NV
HOU.SEC.CON - October 2023, Houston, TX

## How to use it:
1. Run mfcuk to crack a sector A key
2. Run mfoc to get all the keys in the card, dump them out
3. Run nfc-mfclassic to write the source dump onto destination card.

To build the image:
`docker build -t mifare -f Dockerfile .`

To run the built image with the device attached:
`docker run -it --rm --device=/dev/ttyUSB0 mifare`

The following commands are available: 
1. `info` - Get some details about your card (runs `nfc-poll` and will wait till you tap your card) 
2. `read` - Read the data from your card (runs `hexdump` on a .mfd file)
3. `crack` - Retrieve the keys from your card (runs `mfcuk` NOTE: This can take a while to run)
4. `dump` -  Get all the data on the card in hex format (runs `mfoc` and dumps the data to a .mfd file)
5. `help` - Show this exact help message
6. `exit` - Exit the program (will also exit the docker container) 