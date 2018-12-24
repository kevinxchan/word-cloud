# Word cloud pipeline

A simple pipeline to generate a word cloud between you and another individual from [Facebook messenger][fb-msg] messages and from Android SMS messages.

## Steps

1. Get a copy of the Facebook messages/conversation of interest. This can be done by logging into Facebook, and then going to Settings -> Your Facebook Information -> Download Your Information, and then selecting Messages. **Make sure you download the conversations in JSON**.

2. Get a copy of your SMS messages. If you have an Android phone, you can download [SMS Backup & Restore][sms-app] and follow the steps to back-up/copy your messages. **Make sure you download the conversations in XML**.

3. Pass the JSON and XML messages to the script `parser.py`, which will convert these formats into plain text format in a file named `plain.txt`. Example usage:

	```
	python parser.py -x /path/to/xml/convo_foo.xml -j /path/to/json/convo_foo.json -o /out/path
	```

4. Go online and pick from any of the myriad word cloud visualizers out there that accept plain text files as input, and upload `plain.txt` to visualize it. I like [Tag Crowd][ag-crowd] since it allows some options for how to treat different words (ex: word frequencies, excluding words, etc.). If you're looking for a particular shape, [Word Art][word-art] has a bunch. Note however, that the images may be slightly worse quality unless you pay for downloading in HQ.

[fb-msg]: https://www.messenger.com/
[sms-app]: https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en
[tag-crowd]: https://tagcrowd.com/
[word-art]: https://wordart.com/