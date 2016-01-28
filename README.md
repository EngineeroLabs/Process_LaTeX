# LaTeX in Word Server

LaTeX in Word is a GPL-licensed tool that allows equations to be used in
Microsoft Word documents. The client-side of the program is implemented as VBA
macros and can be found in a separate package. In contrast, this package
contains the server-side files in the form of the tarball
"Process\_LaTeX.tar.gz". It is recommended that you read the Word document in
the client-side package before creating your own LaTeX in Word server. For
casual use, the default server may be sufficient.

Briefly, installation consists of installing PERL, PHP, LaTeX, dvipng, and
ImageMagick on a \*nix web server. The LaTeX in Word web server can then be
cloned with:

    git clone https://github.com/Engineero/Process_LaTeX.git

This will create a "Process\_LaTeX" subdirectory immediately below the current
directory. Hence, the current directory should be one that can be accessed by
web users. For example, on some systems this directory could be "public-web" or
one of its subdirectories. The permissions of the extracted files will then
have to be changed so that web users can execute the scripts. For example, in a
particular installation that treats anonymous web users as being in the same
group as the files' owner, the following permissions were used:

    drwxr-xr-x  .
    -rw-r--r--  Delete_Temporary_Files.php
    -rw-r--r--  LaTeX_Converter.pl
    -rw-r--r--  Process_LaTeX.php
    -rw-r--r--  template.tex
    drwxrwxr-x  temporary

The additional 0-byte file "temporary/placeholder" exists only to ensure that
the "temporary" directory is stored in the tarball, so this file can be deleted
after extraction. Since the other files are written in PERL, PHP, and LaTeX,
there is no separate source code.

Complete license information can be found in the file "gpl.txt" stored in this
package. A list of recent changes can be found in "changelog.txt". Updates and
additional information can be found on the GitHub project page:

<https://github.com/Engineero/Process_LaTeX>

