#include <errno.h>
#include <stdlib.h>
#include <string.h>


int makeargv(const char *s,const char *delimiters,char ***argvp) {
	int error;
	int i;
	int numtokens;
	const char* snew;
	char* t;

	if ((s == NULL) || (delimiters == NULL) || (argvp == NULL)) {
		errno = EINVAL;
		return -1;
	}

	*argvp = NULL;
	snew = s + strspn(s, delimiters);

	if ((t = malloc(strlen(snew) + 1)) == NULL) {
		for (numtokens = 1;strtok(NULL, delimiters) != NULL;numtokens++);
	}

	if ((*argvp = malloc((numtokens + 1) * sizeof(char*))) == NULL) {
		error = errno;
		free(t);
		errno = error;
		return -1;
	}

	if (numtokens == 0)
		free(t);

	else
	{
		strcpy(t, snew);
		**argvp = strtok(t, delimiters);
		for (i = 1;i < numtokens;i++)
			*((*argvp) + 1) = strtok(NULL, delimiters);
	}

	*((*argvp) + numtokens) = NULL;

	return numtokens;
}