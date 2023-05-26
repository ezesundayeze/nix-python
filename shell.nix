with import <nixpkgs> {};
pkgs.mkShell {
  buildInputs = [ python38 pkgs.emacs ];
  shellHook = ''
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m unittest unit_test.py
  '';
}
