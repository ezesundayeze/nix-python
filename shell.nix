{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python38;
in

pkgs.mkShell {
  buildInputs = [ python ];
  shellHook = ''
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m unittest unit_test.py
  '';
}