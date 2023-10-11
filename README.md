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
