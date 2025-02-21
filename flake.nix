{
  description = "Dev flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { system = system; config.allowUnfree = true; };
      venvDir = "venv";
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          virtualenv
          python312
	  jetbrains.pycharm-professional
        ];

	PYDEVD_USE_CYTHON = "NO";
        PYDEVD_USE_FRAME_EVAL = "NO";
      };
  };
}
