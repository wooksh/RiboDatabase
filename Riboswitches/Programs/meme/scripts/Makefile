# Makefile.in generated by automake 1.15 from Makefile.am.
# scripts/Makefile.  Generated from Makefile.in by configure.

# Copyright (C) 1994-2014 Free Software Foundation, Inc.

# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.




am__is_gnu_make = { \
  if test -z '$(MAKELEVEL)'; then \
    false; \
  elif test -n '$(MAKE_HOST)'; then \
    true; \
  elif test -n '$(MAKE_VERSION)' && test -n '$(CURDIR)'; then \
    true; \
  else \
    false; \
  fi; \
}
am__make_running_with_option = \
  case $${target_option-} in \
      ?) ;; \
      *) echo "am__make_running_with_option: internal error: invalid" \
              "target option '$${target_option-}' specified" >&2; \
         exit 1;; \
  esac; \
  has_opt=no; \
  sane_makeflags=$$MAKEFLAGS; \
  if $(am__is_gnu_make); then \
    sane_makeflags=$$MFLAGS; \
  else \
    case $$MAKEFLAGS in \
      *\\[\ \	]*) \
        bs=\\; \
        sane_makeflags=`printf '%s\n' "$$MAKEFLAGS" \
          | sed "s/$$bs$$bs[$$bs $$bs	]*//g"`;; \
    esac; \
  fi; \
  skip_next=no; \
  strip_trailopt () \
  { \
    flg=`printf '%s\n' "$$flg" | sed "s/$$1.*$$//"`; \
  }; \
  for flg in $$sane_makeflags; do \
    test $$skip_next = yes && { skip_next=no; continue; }; \
    case $$flg in \
      *=*|--*) continue;; \
        -*I) strip_trailopt 'I'; skip_next=yes;; \
      -*I?*) strip_trailopt 'I';; \
        -*O) strip_trailopt 'O'; skip_next=yes;; \
      -*O?*) strip_trailopt 'O';; \
        -*l) strip_trailopt 'l'; skip_next=yes;; \
      -*l?*) strip_trailopt 'l';; \
      -[dEDm]) skip_next=yes;; \
      -[JT]) skip_next=yes;; \
    esac; \
    case $$flg in \
      *$$target_option*) has_opt=yes; break;; \
    esac; \
  done; \
  test $$has_opt = yes
am__make_dryrun = (target_option=n; $(am__make_running_with_option))
am__make_keepgoing = (target_option=k; $(am__make_running_with_option))
pkgdatadir = $(datadir)/meme
pkgincludedir = $(includedir)/meme
pkglibdir = $(libdir)/meme
pkglibexecdir = $(libexecdir)/meme
am__cd = CDPATH="$${ZSH_VERSION+.}$(PATH_SEPARATOR)" && cd
install_sh_DATA = $(install_sh) -c -m 644
install_sh_PROGRAM = $(install_sh) -c
install_sh_SCRIPT = $(install_sh) -c
INSTALL_HEADER = $(INSTALL_DATA)
transform = $(program_transform_name)
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
build_triplet = x86_64-unknown-linux-gnu
host_triplet = x86_64-unknown-linux-gnu
am__append_1 = dreme \
  fasta-dinucleotide-shuffle \
  fasta-hamming-enrich

am__append_2 = dreme-py3 \
  fasta-dinucleotide-shuffle-py3 \
  fasta-hamming-enrich-py3


# WEBSITE OR WEBSERVICE
#am__append_3 = $(DUALUSE_SERVICES)
#am__append_4 = $(DUALUSE_SERVICES)
#am__append_5 = $(WEBSERVICE_SERVICES)
#am__append_6 = $(WEBSITE_WEBUTILS)
subdir = scripts
ACLOCAL_M4 = $(top_srcdir)/aclocal.m4
am__aclocal_m4_deps = $(top_srcdir)/m4/libtool.m4 \
	$(top_srcdir)/m4/ltoptions.m4 $(top_srcdir)/m4/ltsugar.m4 \
	$(top_srcdir)/m4/ltversion.m4 $(top_srcdir)/m4/lt~obsolete.m4 \
	$(top_srcdir)/configure.ac
am__configure_deps = $(am__aclocal_m4_deps) $(CONFIGURE_DEPENDENCIES) \
	$(ACLOCAL_M4)
DIST_COMMON = $(srcdir)/Makefile.am $(am__DIST_COMMON)
mkinstalldirs = $(SHELL) $(top_srcdir)/config/mkinstalldirs
CONFIG_HEADER = $(top_builddir)/config.h
CONFIG_CLEAN_FILES =
CONFIG_CLEAN_VPATH_FILES =
am__vpath_adj_setup = srcdirstrip=`echo "$(srcdir)" | sed 's|.|.|g'`;
am__vpath_adj = case $$p in \
    $(srcdir)/*) f=`echo "$$p" | sed "s|^$$srcdirstrip/||"`;; \
    *) f=$$p;; \
  esac;
am__strip_dir = f=`echo $$p | sed -e 's|^.*/||'`;
am__install_max = 40
am__nobase_strip_setup = \
  srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*|]/\\\\&/g'`
am__nobase_strip = \
  for p in $$list; do echo "$$p"; done | sed -e "s|$$srcdirstrip/||"
am__nobase_list = $(am__nobase_strip_setup); \
  for p in $$list; do echo "$$p $$p"; done | \
  sed "s| $$srcdirstrip/| |;"' / .*\//!s/ .*/ ./; s,\( .*\)/[^/]*$$,\1,' | \
  $(AWK) 'BEGIN { files["."] = "" } { files[$$2] = files[$$2] " " $$1; \
    if (++n[$$2] == $(am__install_max)) \
      { print $$2, files[$$2]; n[$$2] = 0; files[$$2] = "" } } \
    END { for (dir in files) print dir, files[dir] }'
am__base_list = \
  sed '$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;s/\n/ /g' | \
  sed '$$!N;$$!N;$$!N;$$!N;s/\n/ /g'
am__uninstall_files_from_dir = { \
  test -z "$$files" \
    || { test ! -d "$$dir" && test ! -f "$$dir" && test ! -r "$$dir"; } \
    || { echo " ( cd '$$dir' && rm -f" $$files ")"; \
         $(am__cd) "$$dir" && rm -f $$files; }; \
  }
am__installdirs = "$(DESTDIR)$(bindir)" "$(DESTDIR)$(perlmoddir)" \
	"$(DESTDIR)$(pythonlibdir)"
SCRIPTS = $(bin_SCRIPTS) $(perlmod_SCRIPTS) $(pythonlib_SCRIPTS)
AM_V_P = $(am__v_P_$(V))
am__v_P_ = $(am__v_P_$(AM_DEFAULT_VERBOSITY))
am__v_P_0 = false
am__v_P_1 = :
AM_V_GEN = $(am__v_GEN_$(V))
am__v_GEN_ = $(am__v_GEN_$(AM_DEFAULT_VERBOSITY))
am__v_GEN_0 = @echo "  GEN     " $@;
am__v_GEN_1 = 
AM_V_at = $(am__v_at_$(V))
am__v_at_ = $(am__v_at_$(AM_DEFAULT_VERBOSITY))
am__v_at_0 = @
am__v_at_1 = 
SOURCES =
DIST_SOURCES =
am__can_run_installinfo = \
  case $$AM_UPDATE_INFO_DIR in \
    n|no|NO) false;; \
    *) (install-info --version) >/dev/null 2>&1;; \
  esac
am__tagged_files = $(HEADERS) $(SOURCES) $(TAGS_FILES) $(LISP)
am__DIST_COMMON = $(srcdir)/Makefile.in \
	$(top_srcdir)/config/mkinstalldirs README
DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)
ACLOCAL = ${SHELL} /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/config/missing aclocal-1.15
AMTAR = $${TAR-tar}
AM_DEFAULT_VERBOSITY = 1
ANT = 
AR = ar
AUTOCONF = ${SHELL} /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/config/missing autoconf
AUTOHEADER = ${SHELL} /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/config/missing autoheader
AUTOMAKE = ${SHELL} /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/config/missing automake-1.15
AWK = mawk
CATALINA_HOME = 
CC = gcc
CCDEPMODE = depmode=gcc3
CFLAGS = -std=gnu89 -Wall -Wno-unused -DUNIX -D__USE_FIXED_PROTOTYPES__   -O3
CONTACT = 
CONVERT = /usr/bin/convert
CPP = gcc -E
CPPFLAGS = 
CYGPATH_W = echo
DEBUG_FLAGS = 
DEFS = -DHAVE_CONFIG_H
DEPDIR = .deps
DEV_CONTACT = meme-suite@uw.edu
DLLTOOL = false
DSYMUTIL = 
DUMPBIN = 
ECHO_C = 
ECHO_N = -n
ECHO_T = 
EGREP = /bin/grep -E
EXEEXT = 
EXPIRY = 4
FGREP = /bin/grep -F
GHOSTSCRIPT = /usr/bin/gs
GOSERVER_URL = http://amigo.geneontology.org/cgi-bin/amigo/term_details?term=GO_TERM_ID
GREP = /bin/grep
HOSTNAME = alcedo-X555LD
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL_STRIP_PROGRAM = $(install_sh) -c -s
LAMBIN = 
LD = /usr/bin/ld -m elf_x86_64
LDFLAGS = 
LIBEXSLT_CFLAGS = -I${top_srcdir}/src/libexslt
LIBEXSLT_LIBS = ${top_builddir}/src/libexslt/libexslt.la
LIBOBJS = 
LIBS = -lm 
LIBTOOL = $(SHELL) $(top_builddir)/libtool
LIBXML2_CFLAGS = -I${top_srcdir}/src/libxml2/include
LIBXML2_LIBS = ${top_builddir}/src/libxml2/libxml2.la
LIBXSLT_CFLAGS = -I${top_srcdir}/src/
LIBXSLT_LIBS = ${top_builddir}/src/libxslt/libxslt.la
LIPO = 
LN_S = ln -s
LTLIBOBJS = 
LT_SYS_LIBRARY_PATH = 
MACHID = linux
MAKEINFO = ${SHELL} /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/config/missing makeinfo
MANIFEST_TOOL = :
MAST_PORT = 
MAXTIME = 18000
MEME_DB = ${prefix}/db
MEME_DIRECTORY = ${prefix}
MEME_LOGS = ${prefix}/LOGS
MEME_PORT = 
MEME_TEMP = 
MKDIR_P = /bin/mkdir -p
MPICC = gcc
MPIFLAGS = 
MPIINC = 
MPILIBDIR = 
MPIRUN = 
MPITYPE = 
MPI_CMD = 
NEWS_URL = ./news.txt
NM = /usr/bin/nm -B
NMEDIT = 
NOTICES_URL = ./notices.txt
OBJDUMP = objdump
OBJEXT = o
OPAL_DEPLOY = 
OPAL_URL = no
OPT_FLAGS = -O3
OTOOL = 
OTOOL64 = 
PACKAGE = meme
PACKAGE_BUGREPORT = 
PACKAGE_NAME = meme
PACKAGE_STRING = meme 4.12.0
PACKAGE_TARNAME = meme
PACKAGE_URL = 
PACKAGE_VERSION = 4.12.0
PATH_SEPARATOR = :
PERL = /usr/bin/perl
PREV_URL = 
PREV_VER = 
PYTHON = /usr/bin/python
PYTHON3 = /usr/bin/python3
QUOTA = 
RANLIB = ranlib
SED = /bin/sed
SENDMAIL = /usr/lib/sendmail
SET_MAKE = 
SHELL = /bin/bash
STRIP = strip
URL = http://meme-suite.org
VERSION = 4.12.0
WEBSERVICE = 
XML2_CONFIG = 
XSLT_CONFIG = 
abs_builddir = /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/scripts
abs_srcdir = /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/scripts
abs_top_builddir = /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0
abs_top_srcdir = /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0
ac_ct_AR = ar
ac_ct_CC = gcc
ac_ct_DUMPBIN = 
am__include = include
am__leading_dot = .
am__quote = 
am__tar = $${TAR-tar} chof - "$$tardir"
am__untar = $${TAR-tar} xf -
bindir = ${exec_prefix}/bin
build = x86_64-unknown-linux-gnu
build_alias = 
build_cpu = x86_64
build_os = linux-gnu
build_vendor = unknown
builddir = .
datadir = ${datarootdir}
datarootdir = ${prefix}/share
docdir = ${datarootdir}/doc/${PACKAGE_TARNAME}
dvidir = ${docdir}
exec_prefix = ${prefix}
host = x86_64-unknown-linux-gnu
host_alias = 
host_cpu = x86_64
host_os = linux-gnu
host_vendor = unknown
htmldir = ${docdir}
includedir = ${prefix}/include
infodir = ${datarootdir}/info
install_sh = ${SHELL} /home/alcedo/Desktop/Github/RiboDatabase/Riboswitches/Programs/meme_4.12.0/config/install-sh
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/libexec
localedir = ${datarootdir}/locale
localstatedir = ${prefix}/var
mandir = ${datarootdir}/man
mkdir_p = $(MKDIR_P)
oldincludedir = /usr/include
pdfdir = ${docdir}
prefix = /root/meme
program_transform_name = s,x,x,
psdir = ${docdir}
sbindir = ${exec_prefix}/sbin
sharedstatedir = ${prefix}/com
srcdir = .
sysconfdir = ${prefix}/etc
target_alias = 
top_build_prefix = ../
top_builddir = ..
top_srcdir = ..
MEME_DOC_DIR = $(prefix)/doc

# Set installation location for doc files.
#MEME_DOC_DIR = $(WEBDIR)/doc
ARCHIVE_REVISION = $(shell cat ../ARCHIVE_REVISION)
ARCHIVE_DATE = $(shell cat ../ARCHIVE_DATE)
SEDSPEC = \
  -e 's%@ARCHIVE_REVISION@%$(ARCHIVE_REVISION)%' \
  -e 's%@ARCHIVE_DATE@%$(ARCHIVE_DATE)%' \
  -e 's%@ARCHIVE_VERSION@%$(VERSION)%' \
  -e 's%@TMP_DIR@%$(MEME_TEMP)%' \
  -e 's%@WHICHPERL@%$(PERL)%' \
  -e 's%@WHICHPYTHON@%$(PYTHON)%' \
  -e 's%@WHICHPYTHON3@%$(PYTHON3)%' \
  -e 's%@WHICHJAVA@%$(JAVA)%' \
  -e 's%@WHICHCONVERT@%$(CONVERT)%' \
  -e 's%@WHICHGHOSTSCRIPT@%$(GHOSTSCRIPT)%' \
  -e 's%@PERLLIBDIR@%$(libdir)/perl%' \
  -e 's%@PYTHONLIBDIR@%$(libdir)/python%' \
  -e 's%@JAVALIBDIR@%$(libdir)/java%' \
  -e 's%@LAM_BIN@%$(LAMBIN)%' \
  -e 's%@APPCONFIGDIR@%$(sysconfdir)%' \
  -e 's%@BINDIR@%$(bindir)%' \
  -e 's%@MEMELOGS@%$(MEME_LOGS)%' \
  -e 's%@MEMEDB@%$(MEME_DB)%' \
  -e 's%@SITE_URL@%$(URL)%' \
  -e 's%@MAX_TIME@%$(MAXTIME)%' \
  -e 's%@DOCDIR@%$(MEME_DOC_DIR)/%'

BUILT_PERL_MOD = \
  Globals.pm \
  MemeWebUtils.pm \
  StatusPage.pm

NORMAL_PERL_MOD = \
  Alphabet.pm \
  CheckingSAX.pm \
  DremeSAX.pm \
  ExecUtils.pm \
  HtmlMonolithWr.pm \
  JsonRdr.pm \
  JsonWr.pm \
  MastSAX.pm \
  MemeSAX.pm \
  MotifInDremeXML.pm \
  MotifInMemeXML.pm \
  MotifUtils.pm \
  PriorUtils.pm \
  ReadFastaFile.pm \
  TomtomSAX.pm

OTHER_PERL_MOD = \
  CombDynProg.pm \
  DiffJSON.pm \
  DiffXML.pm \
  HypergeometricDynProg.pm

perlmoddir = $(libdir)/perl
perlmod_SCRIPTS = \
  $(BUILT_PERL_MOD) \
  $(NORMAL_PERL_MOD)

NORMAL_PYTHON_LIB_SRC = \
  alphabet.py \
  hypergeometric.py \
  sequence.py

BUILT_PYTHON_LIB_SRC = \
  fasta-dinucleotide-shuffle.py \
  fasta-hamming-enrich.py

NORMAL_PYTHON3_LIB_SRC = \
  alphabet_py3.py \
  hypergeometric_py3.py \
  sequence_py3.py

BUILT_PYTHON3_LIB_SRC = \
  fasta-dinucleotide-shuffle-py3.py \
  fasta-hamming-enrich-py3.py

NORMAL_PYTHON_LIB := $(NORMAL_PYTHON_LIB_SRC)
BUILT_PYTHON_LIB := $(BUILT_PYTHON_LIB_SRC)
NORMAL_PYTHON3_LIB := $(NORMAL_PYTHON3_LIB_SRC)
BUILT_PYTHON3_LIB := $(BUILT_PYTHON3_LIB_SRC)
pythonlibdir = $(libdir)/python
pythonlib_SCRIPTS = \
  $(BUILT_PYTHON_LIB) \
  $(NORMAL_PYTHON_LIB) \
  $(BUILT_PYTHON3_LIB) \
  $(NORMAL_PYTHON3_LIB)

INPUT_FILES = $(wildcard *.in)
BUILT_UTILS = ama-qvalues beeml2meme dreme_xml_to_html \
	dreme_xml_to_txt elm2meme fasta-center \
	fasta-dinucleotide-shuffle fasta-fetch fasta-hamming-enrich \
	fasta-make-index fasta-most fasta-re-match fasta-subsample \
	fasta-unique-names glam2html glam2psfm glam2scan2html \
	chen2meme jaspar2meme hart2meme-bkg hartemink2psp iupac2meme \
	mast_xml_to_html mast_xml_to_txt matrix2meme meme-chip \
	meme-chip_html_to_tsv meme-rename meme_xml_to_html nmica2meme \
	priority2meme psp-gen rsat-retrieve-seq \
	rsat-supported-organisms rna2meme scpd2meme sites2meme \
	taipale2meme tamo2meme tomtom_xml_to_html transfac2meme \
	uniprobe2meme $(am__append_1) $(am__append_2)
UTILS = \
	fasta-grep \
  plotgen \
  sd \
  $(BUILT_UTILS)

OBSOLETE_UTILS = \
  fasta-enriched-center \
  mhmm2html


# services
DUALUSE_SERVICES = \
  tomtom_webservice

WEBSERVICE_SERVICES = \
  ame_webservice \
  centrimo_webservice \
  dreme_webservice \
  fimo_webservice \
  glam2scan_webservice \
  glam2_webservice \
  gomo_webservice \
  mast_webservice \
  mcast_webservice \
  meme-chip_webservice \
  meme_webservice \
  momo_webservice \
  spamo_webservice


#utilities
WEBSITE_BUILT_WEBUTILS = \
  lrun \
  texit \
  update-plot-usage \
  update-sequence-db

WEBSITE_WEBUTILS = \
  plot-usage \
  usage-reports \
  $(WEBSITE_BUILT_WEBUTILS)

MEME_SERVICES = $(am__append_3) $(am__append_4) $(am__append_5)
MEME_WEBUTILS = $(am__append_6)

# Set automake targets
bin_SCRIPTS = $(UTILS) $(MEME_WEBUTILS) $(MEME_SERVICES)

# Define which files to delete if target is 'make clean'.
CLEANFILES = \
  $(BUILT_PERL_MOD) \
  $(BUILT_PYTHON_LIB) \
  $(BUILT_PYTHON3_LIB) \
  $(BUILT_UTILS) \
  $(WEBSITE_BUILT_WEBUTILS) \
  $(MEME_SERVICES)

EXTRA_DIST = \
  $(NORMAL_PERL_MOD) \
  $(OTHER_PERL_MOD) \
  $(NORMAL_PYTHON_LIB_SRC) \
  $(NORMAL_PYTHON3_LIB_SRC) \
  dependencies.pl \
	fasta-grep \
  obo2dag.jar \
  plotgen \
  plot-usage \
  sd \
  usage-reports \
  $(INPUT_FILES)

all: all-am

.SUFFIXES:
$(srcdir)/Makefile.in:  $(srcdir)/Makefile.am  $(am__configure_deps)
	@for dep in $?; do \
	  case '$(am__configure_deps)' in \
	    *$$dep*) \
	      ( cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh ) \
	        && { if test -f $@; then exit 0; else break; fi; }; \
	      exit 1;; \
	  esac; \
	done; \
	echo ' cd $(top_srcdir) && $(AUTOMAKE) --gnu scripts/Makefile'; \
	$(am__cd) $(top_srcdir) && \
	  $(AUTOMAKE) --gnu scripts/Makefile
Makefile: $(srcdir)/Makefile.in $(top_builddir)/config.status
	@case '$?' in \
	  *config.status*) \
	    cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh;; \
	  *) \
	    echo ' cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe)'; \
	    cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe);; \
	esac;

$(top_builddir)/config.status: $(top_srcdir)/configure $(CONFIG_STATUS_DEPENDENCIES)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh

$(top_srcdir)/configure:  $(am__configure_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(ACLOCAL_M4):  $(am__aclocal_m4_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(am__aclocal_m4_deps):
install-binSCRIPTS: $(bin_SCRIPTS)
	@$(NORMAL_INSTALL)
	@list='$(bin_SCRIPTS)'; test -n "$(bindir)" || list=; \
	if test -n "$$list"; then \
	  echo " $(MKDIR_P) '$(DESTDIR)$(bindir)'"; \
	  $(MKDIR_P) "$(DESTDIR)$(bindir)" || exit 1; \
	fi; \
	for p in $$list; do \
	  if test -f "$$p"; then d=; else d="$(srcdir)/"; fi; \
	  if test -f "$$d$$p"; then echo "$$d$$p"; echo "$$p"; else :; fi; \
	done | \
	sed -e 'p;s,.*/,,;n' \
	    -e 'h;s|.*|.|' \
	    -e 'p;x;s,.*/,,;$(transform)' | sed 'N;N;N;s,\n, ,g' | \
	$(AWK) 'BEGIN { files["."] = ""; dirs["."] = 1; } \
	  { d=$$3; if (dirs[d] != 1) { print "d", d; dirs[d] = 1 } \
	    if ($$2 == $$4) { files[d] = files[d] " " $$1; \
	      if (++n[d] == $(am__install_max)) { \
		print "f", d, files[d]; n[d] = 0; files[d] = "" } } \
	    else { print "f", d "/" $$4, $$1 } } \
	  END { for (d in files) print "f", d, files[d] }' | \
	while read type dir files; do \
	     if test "$$dir" = .; then dir=; else dir=/$$dir; fi; \
	     test -z "$$files" || { \
	       echo " $(INSTALL_SCRIPT) $$files '$(DESTDIR)$(bindir)$$dir'"; \
	       $(INSTALL_SCRIPT) $$files "$(DESTDIR)$(bindir)$$dir" || exit $$?; \
	     } \
	; done

uninstall-binSCRIPTS:
	@$(NORMAL_UNINSTALL)
	@list='$(bin_SCRIPTS)'; test -n "$(bindir)" || exit 0; \
	files=`for p in $$list; do echo "$$p"; done | \
	       sed -e 's,.*/,,;$(transform)'`; \
	dir='$(DESTDIR)$(bindir)'; $(am__uninstall_files_from_dir)
install-perlmodSCRIPTS: $(perlmod_SCRIPTS)
	@$(NORMAL_INSTALL)
	@list='$(perlmod_SCRIPTS)'; test -n "$(perlmoddir)" || list=; \
	if test -n "$$list"; then \
	  echo " $(MKDIR_P) '$(DESTDIR)$(perlmoddir)'"; \
	  $(MKDIR_P) "$(DESTDIR)$(perlmoddir)" || exit 1; \
	fi; \
	for p in $$list; do \
	  if test -f "$$p"; then d=; else d="$(srcdir)/"; fi; \
	  if test -f "$$d$$p"; then echo "$$d$$p"; echo "$$p"; else :; fi; \
	done | \
	sed -e 'p;s,.*/,,;n' \
	    -e 'h;s|.*|.|' \
	    -e 'p;x;s,.*/,,;$(transform)' | sed 'N;N;N;s,\n, ,g' | \
	$(AWK) 'BEGIN { files["."] = ""; dirs["."] = 1; } \
	  { d=$$3; if (dirs[d] != 1) { print "d", d; dirs[d] = 1 } \
	    if ($$2 == $$4) { files[d] = files[d] " " $$1; \
	      if (++n[d] == $(am__install_max)) { \
		print "f", d, files[d]; n[d] = 0; files[d] = "" } } \
	    else { print "f", d "/" $$4, $$1 } } \
	  END { for (d in files) print "f", d, files[d] }' | \
	while read type dir files; do \
	     if test "$$dir" = .; then dir=; else dir=/$$dir; fi; \
	     test -z "$$files" || { \
	       echo " $(INSTALL_SCRIPT) $$files '$(DESTDIR)$(perlmoddir)$$dir'"; \
	       $(INSTALL_SCRIPT) $$files "$(DESTDIR)$(perlmoddir)$$dir" || exit $$?; \
	     } \
	; done

uninstall-perlmodSCRIPTS:
	@$(NORMAL_UNINSTALL)
	@list='$(perlmod_SCRIPTS)'; test -n "$(perlmoddir)" || exit 0; \
	files=`for p in $$list; do echo "$$p"; done | \
	       sed -e 's,.*/,,;$(transform)'`; \
	dir='$(DESTDIR)$(perlmoddir)'; $(am__uninstall_files_from_dir)
install-pythonlibSCRIPTS: $(pythonlib_SCRIPTS)
	@$(NORMAL_INSTALL)
	@list='$(pythonlib_SCRIPTS)'; test -n "$(pythonlibdir)" || list=; \
	if test -n "$$list"; then \
	  echo " $(MKDIR_P) '$(DESTDIR)$(pythonlibdir)'"; \
	  $(MKDIR_P) "$(DESTDIR)$(pythonlibdir)" || exit 1; \
	fi; \
	for p in $$list; do \
	  if test -f "$$p"; then d=; else d="$(srcdir)/"; fi; \
	  if test -f "$$d$$p"; then echo "$$d$$p"; echo "$$p"; else :; fi; \
	done | \
	sed -e 'p;s,.*/,,;n' \
	    -e 'h;s|.*|.|' \
	    -e 'p;x;s,.*/,,;$(transform)' | sed 'N;N;N;s,\n, ,g' | \
	$(AWK) 'BEGIN { files["."] = ""; dirs["."] = 1; } \
	  { d=$$3; if (dirs[d] != 1) { print "d", d; dirs[d] = 1 } \
	    if ($$2 == $$4) { files[d] = files[d] " " $$1; \
	      if (++n[d] == $(am__install_max)) { \
		print "f", d, files[d]; n[d] = 0; files[d] = "" } } \
	    else { print "f", d "/" $$4, $$1 } } \
	  END { for (d in files) print "f", d, files[d] }' | \
	while read type dir files; do \
	     if test "$$dir" = .; then dir=; else dir=/$$dir; fi; \
	     test -z "$$files" || { \
	       echo " $(INSTALL_SCRIPT) $$files '$(DESTDIR)$(pythonlibdir)$$dir'"; \
	       $(INSTALL_SCRIPT) $$files "$(DESTDIR)$(pythonlibdir)$$dir" || exit $$?; \
	     } \
	; done

uninstall-pythonlibSCRIPTS:
	@$(NORMAL_UNINSTALL)
	@list='$(pythonlib_SCRIPTS)'; test -n "$(pythonlibdir)" || exit 0; \
	files=`for p in $$list; do echo "$$p"; done | \
	       sed -e 's,.*/,,;$(transform)'`; \
	dir='$(DESTDIR)$(pythonlibdir)'; $(am__uninstall_files_from_dir)

mostlyclean-libtool:
	-rm -f *.lo

clean-libtool:
	-rm -rf .libs _libs
tags TAGS:

ctags CTAGS:

cscope cscopelist:


distdir: $(DISTFILES)
	@srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	topsrcdirstrip=`echo "$(top_srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	list='$(DISTFILES)'; \
	  dist_files=`for file in $$list; do echo $$file; done | \
	  sed -e "s|^$$srcdirstrip/||;t" \
	      -e "s|^$$topsrcdirstrip/|$(top_builddir)/|;t"`; \
	case $$dist_files in \
	  */*) $(MKDIR_P) `echo "$$dist_files" | \
			   sed '/\//!d;s|^|$(distdir)/|;s,/[^/]*$$,,' | \
			   sort -u` ;; \
	esac; \
	for file in $$dist_files; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  if test -d $$d/$$file; then \
	    dir=`echo "/$$file" | sed -e 's,/[^/]*$$,,'`; \
	    if test -d "$(distdir)/$$file"; then \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -fpR $(srcdir)/$$file "$(distdir)$$dir" || exit 1; \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    cp -fpR $$d/$$file "$(distdir)$$dir" || exit 1; \
	  else \
	    test -f "$(distdir)/$$file" \
	    || cp -p $$d/$$file "$(distdir)/$$file" \
	    || exit 1; \
	  fi; \
	done
check-am: all-am
check: check-am
all-am: Makefile $(SCRIPTS)
installdirs:
	for dir in "$(DESTDIR)$(bindir)" "$(DESTDIR)$(perlmoddir)" "$(DESTDIR)$(pythonlibdir)"; do \
	  test -z "$$dir" || $(MKDIR_P) "$$dir"; \
	done
install: install-am
install-exec: install-exec-am
install-data: install-data-am
uninstall: uninstall-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-am
install-strip:
	if test -z '$(STRIP)'; then \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	      install; \
	else \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	    "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'" install; \
	fi
mostlyclean-generic:

clean-generic:
	-test -z "$(CLEANFILES)" || rm -f $(CLEANFILES)

distclean-generic:
	-test -z "$(CONFIG_CLEAN_FILES)" || rm -f $(CONFIG_CLEAN_FILES)
	-test . = "$(srcdir)" || test -z "$(CONFIG_CLEAN_VPATH_FILES)" || rm -f $(CONFIG_CLEAN_VPATH_FILES)

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
clean: clean-am

clean-am: clean-generic clean-libtool mostlyclean-am

distclean: distclean-am
	-rm -f Makefile
distclean-am: clean-am distclean-generic

dvi: dvi-am

dvi-am:

html: html-am

html-am:

info: info-am

info-am:

install-data-am: install-perlmodSCRIPTS install-pythonlibSCRIPTS

install-dvi: install-dvi-am

install-dvi-am:

install-exec-am: install-binSCRIPTS

install-html: install-html-am

install-html-am:

install-info: install-info-am

install-info-am:

install-man:

install-pdf: install-pdf-am

install-pdf-am:

install-ps: install-ps-am

install-ps-am:

installcheck-am:

maintainer-clean: maintainer-clean-am
	-rm -f Makefile
maintainer-clean-am: distclean-am maintainer-clean-generic

mostlyclean: mostlyclean-am

mostlyclean-am: mostlyclean-generic mostlyclean-libtool

pdf: pdf-am

pdf-am:

ps: ps-am

ps-am:

uninstall-am: uninstall-binSCRIPTS uninstall-perlmodSCRIPTS \
	uninstall-pythonlibSCRIPTS

.MAKE: install-am install-strip

.PHONY: all all-am check check-am clean clean-generic clean-libtool \
	cscopelist-am ctags-am distclean distclean-generic \
	distclean-libtool distdir dvi dvi-am html html-am info info-am \
	install install-am install-binSCRIPTS install-data \
	install-data-am install-dvi install-dvi-am install-exec \
	install-exec-am install-html install-html-am install-info \
	install-info-am install-man install-pdf install-pdf-am \
	install-perlmodSCRIPTS install-ps install-ps-am \
	install-pythonlibSCRIPTS install-strip installcheck \
	installcheck-am installdirs maintainer-clean \
	maintainer-clean-generic mostlyclean mostlyclean-generic \
	mostlyclean-libtool pdf pdf-am ps ps-am tags-am uninstall \
	uninstall-am uninstall-binSCRIPTS uninstall-perlmodSCRIPTS \
	uninstall-pythonlibSCRIPTS

.PRECIOUS: Makefile


# Describe dependencies and build instructions for scripts.
# (substitute in local path to Perl).

# input files with unusual build names
MemeWebUtils.pm: MemeWebUtils.pm.in Makefile
	$(SED) $(SEDSPEC) $< > $@
StatusPage.pm: StatusPage.pm.in Makefile
	$(SED) $(SEDSPEC) $< > $@
Globals.pm: Globals.pm.in Makefile
	$(SED) $(SEDSPEC) $< > $@

# sh input files
%: %.sh.in
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@

# csh input files
%: %.csh.in
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@

# perl input files
%: %.pl.in
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@

# python input files
%: %.py.in sequence.py hypergeometric.py ../ARCHIVE_DATE ../ARCHIVE_REVISION
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@

# need these to allow use as a Python library or for command line
# Python modules assume a file suffix of .py.
fasta-hamming-enrich.py: fasta-hamming-enrich
	cp fasta-hamming-enrich fasta-hamming-enrich.py
	echo $(BUILT_PYTHON_LIB)
	echo $(NORMAL_PYTHON_LIB)
fasta-dinucleotide-shuffle.py: fasta-dinucleotide-shuffle
	cp fasta-dinucleotide-shuffle fasta-dinucleotide-shuffle.py

# python3 input files
dreme-py3: dreme_py3.py.in alphabet_py3.py sequence_py3.py hypergeometric_py3.py ../ARCHIVE_DATE ../ARCHIVE_REVISION
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@
fasta-dinucleotide-shuffle-py3: fasta-dinucleotide-shuffle-py3.in  ../ARCHIVE_DATE ../ARCHIVE_REVISION
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@
fasta-dinucleotide-shuffle-py3.py: fasta-dinucleotide-shuffle-py3
	cp fasta-dinucleotide-shuffle-py3 fasta-dinucleotide-shuffle-py3.py
fasta-hamming-enrich-py3: fasta-hamming-enrich-py3.in  ../ARCHIVE_DATE ../ARCHIVE_REVISION
	$(SED) $(SEDSPEC) $< > $@; \
  chmod +x $@
fasta-hamming-enrich-py3.py: fasta-hamming-enrich-py3
	cp  fasta-hamming-enrich-py3 fasta-hamming-enrich-py3.py

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
