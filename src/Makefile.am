EXTRA_DIST =
lib_LTLIBRARIES = libnxmodbus.la

AM_CPPFLAGS = \
    -include $(top_builddir)/config.h \
    -DSYSCONFDIR=\""$(sysconfdir)"\" \
    -DLIBEXECDIR=\""$(libexecdir)"\" \
    -I${top_srcdir}/src

AM_CFLAGS = ${my_CFLAGS}

libnxmodbus_la_SOURCES = \
        modbus.c \
        modbus.h \
        modbus-data.c \
        modbus-private.h \
        modbus-rtu.c \
        modbus-rtu.h \
        modbus-rtu-private.h \
        modbus-tcp.c \
        modbus-tcp.h \
        modbus-tcp-private.h \
        modbus-version.h

libnxmodbus_la_LDFLAGS = -no-undefined \
        -version-info $(LIBMODBUS_LT_VERSION_INFO)

if OS_WIN32
libnxmodbus_la_LIBADD = -lwsock32
endif

if OS_QNX
libnxmodbus_la_LIBADD = -lsocket
endif

# Header files to install
libnxmodbusincludedir = $(includedir)/modbus
libnxmodbusinclude_HEADERS = modbus.h modbus-version.h modbus-rtu.h modbus-tcp.h

DISTCLEANFILES = modbus-version.h
EXTRA_DIST += modbus-version.h.in
CLEANFILES = *~
