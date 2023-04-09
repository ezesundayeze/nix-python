{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python38;
in

pkgs.mkShell {
  name = "myenv";
  buildInputs = [ python ];
  shellHook = ''
    python -m venv venv
    source env/bin/activate
    pip install -r requirements.txt
    python -m unittest unit_test.py
  '';
}