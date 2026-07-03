TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    glad.c

INCLUDEPATH += .\
INCLUDEPATH += $$PWD/../../../OpenGLDepMinGW/include
LIBS += -lGLFW3 -lopengl32 -lglu32 -luser32 -lgdi32\

HEADERS += \
    shader_s.h

