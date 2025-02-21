#!/bin/sh
exec nix develop /home/romatthe/Source/Steam-Metadata-Editor/flake.nix --command python "$@"
