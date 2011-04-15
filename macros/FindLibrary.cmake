SET(LIB_TYPE SHARED)

OPTION(BUILD_SHARED_LIBS "Build shared libs" ON)
MARK_AS_ADVANCED(BUILD_SHARED)

IF (BUILD_SHARED)
    SET(LIB_TYPE SHARED)
ELSE()
    SET(LIB_TYPE STATIC)
ENDIF()

STRING(COMPARE NOTEQUAL "${BUILD_SHARED_STATUS}" "" BUILD_SHARED_STATUS_NOT_EMPTY)
IF(BUILD_SHARED_STATUS_NOT_EMPTY)
    STRING(COMPARE NOTEQUAL "${BUILD_SHARED_STATUS}" "${BUILD_SHARED}" RESET)
ENDIF()

# Store in cache previous value of BUILD_SHARED
SET(BUILD_SHARED_STATUS "${BUILD_SHARED}" CACHE INTERNAL "Previous shared status" FORCE)

FUNCTION(FIND_LIBRARY VAR)
    IF(${RESET})
        SET(${VAR} NOTFOUND CACHE STRING "" FORCE)
    ENDIF()
    _FIND_LIBRARY(${VAR} ${ARGN})
    MARK_AS_ADVANCED(${VAR})
ENDFUNCTION()
