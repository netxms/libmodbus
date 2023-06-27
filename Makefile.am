CLEANFILES =
ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}
AM_MAKEFLAGS = --no-print-directory

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libnxmodbus.pc
EXTRA_DIST = libnxmodbus.pc.in
CLEANFILES += libnxmodbus.pc

dist_doc_DATA = AUTHORS NEWS README.md

SUBDIRS = src

if BUILD_TESTS
SUBDIRS += tests
endif
