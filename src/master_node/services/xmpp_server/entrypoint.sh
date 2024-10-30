#!/bin/bash

prosodyctl register user1 localhost password123
prosodyctl register admin localhost securepassword
exec prosody
