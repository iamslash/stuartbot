# About

stuartbot is a chatting bot supports slack, telegram, jandi, etc.

# Features

* recommend movie list
* recommend leetcode problem
* show googleplay app ranks
* ...

# Prerequisites

## Windows

```
choco install chromedriver
cp setapikey.bat.sample setapikey.bat
notepad setapikey.bat
setapikey.bat
```

## Mac

```
brew install chromedriver
cp setapikey.sh.sample setapikey.sh
vim setapikey.sh
source setapikey.sh
```

# How to run

## slack

```
python stuartslack.py
```

## telegram

```
python stuarttele.py
```

## jandi

```
python stuartjandi.py
```
