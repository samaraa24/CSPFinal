{pkgs}: {
  deps = [
    pkgs.xsimd
    pkgs.libxcrypt
    pkgs.glibcLocales
    pkgs.glibc
    pkgs.tk
    pkgs.tcl
    pkgs.qhull
    pkgs.pkg-config
    pkgs.gtk3
    pkgs.gobject-introspection
    pkgs.ghostscript
    pkgs.freetype
    pkgs.ffmpeg-full
    pkgs.cairo
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.xsimd
      pkgs.libxcrypt
      pkgs.glibcLocales
      pkgs.tk
      pkgs.tcl
      pkgs.qhull
      pkgs.gtk3
      pkgs.gobject-introspection
      pkgs.ghostscript
      pkgs.freetype
      pkgs.cairo
    ];
  };
}
