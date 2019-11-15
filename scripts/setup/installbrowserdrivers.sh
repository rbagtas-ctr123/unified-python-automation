#!/usr/bin/env bash

echo "Updating Homebrew recipes..."
brew update

PACKAGES=(
    geckodriver
)

echo "Installing Geckodriver..."
brew install ${PACKAGES[@]}
brew upgrade ${PACKAGES[@]}

echo "Cleaning up..."
brew cleanup

CASKS=(
    firefox
    google-chrome
    chromedriver
)

echo "Installing Firefox, Chrome, and Chrome Driver..."
brew cask install ${CASKS[@]}
brew cask upgrade ${CASKS[@]}
