TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

INCLUDEPATH += .\
INCLUDEPATH += $$PWD/../../../OpenGLDepMinGW/include
LIBS += -lGLFW3 -lopengl32 -lglu32 -luser32 -lgdi32\


SOURCES += main.cpp \
    glad.c
