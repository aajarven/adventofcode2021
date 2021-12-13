#include<stdlib.h>
#include"../c-utils/arrayutils.h"

typedef struct StackNode {
	struct StackNode* next;
	char ch;
} StackNode;

int syntax_score_line(char* line);
long autocomplete_score_line(char* line);

StackNode* create(char ch, StackNode* previous);
void push(StackNode** top, char ch);
char pop(StackNode** top);
void clear(StackNode** top);


int syntax_score(char* data, int max_line_length, int n_lines) {
	int score = 0;
	for (int i=0; i<n_lines; i++) {
		score += syntax_score_line(&data[i*max_line_length]);
	}

	return score;
}

int syntax_score_line(char* line) {
	StackNode* first;
	first = create('\0', NULL);
	StackNode** stack = &first;
	char* current = line;
	while (*current != '\0' && *current != '\n') {
		if (*current == '(' || *current == '[' || *current == '{' || *current == '<') {
			push(stack, *current);
		} else {
			char matching_character = pop(stack);
			if ( !(
					(*current == ')' && matching_character == '(')
					|| (*current == ']' && matching_character == '[')
					|| (*current == '}' && matching_character == '{')
					|| (*current == '>' && matching_character == '<')
				  )) {
				if (*current == ')') {
					clear(stack);
					return 3;
				} else if (*current == ']') {
					clear(stack);
					return 57;
				} else if (*current == '}') {
					clear(stack);
					return 1197;
				} else if (*current == '>') {
					clear(stack);
					return 25137;
				}
			}
		}
				
		current++;
	}
	return 0;
}



long autocomplete_score(char* data, int max_line_length, int n_lines) {
	long scores[n_lines];
	for (int i=0; i<n_lines; i++) {
		scores[i] = autocomplete_score_line(&data[i*max_line_length]);
	}
	quicksort_long(scores, n_lines);

	// find first autocompleted line and take median of the rest
	for (int i=0; i<n_lines; i++) {
		if (scores[i] != 0) {
			return scores[i + (n_lines - i)/2];
		}
	}

	return 0;
}

long autocomplete_score_line(char* line) {
	StackNode* first;
	first = create('\0', NULL);
	StackNode** stack = &first;
	char* current = line;

	// handle all characters there are
	while (*current != '\0' && *current != '\n') {
		if (*current == '(' || *current == '[' || *current == '{' || *current == '<') {
			push(stack, *current);
		} else {
			char matching_character = pop(stack);
			if ( !(
					(*current == ')' && matching_character == '(')
					|| (*current == ']' && matching_character == '[')
					|| (*current == '}' && matching_character == '{')
					|| (*current == '>' && matching_character == '<')
				  )) {
				clear(stack);
				return 0;
			}
		}
		current++;
	}

	long score = 0;
	while (*stack != NULL) {
		int increase = 0;
		if ((*stack)->ch == '(') {
			increase = 1;
		} else if ((*stack)->ch == '[') {
			increase = 2;
		} else if ((*stack)->ch == '{') {
			increase = 3;
		} else if ((*stack)->ch == '<') {
			increase = 4;
		}

		// the first member of stack doesn't have proper data in it, so don't
		// multiply the score by 5 
		if (increase != 0) {
			score = score*5 + increase;
		}
		pop(stack);
	}
	return score;
}


StackNode* create(char ch, StackNode* previous) {
	StackNode* stacknode = malloc(sizeof(StackNode));
	stacknode->next = previous;
	stacknode->ch = ch;
	return stacknode;
}

void push(StackNode** top, char ch) {
	StackNode* new = create(ch, *top);
	*top = new;
}

char pop(StackNode** top) {
	StackNode* popped = *top;
	char popped_character = popped->ch;
	*top = (*top)->next;
	free(popped);
	return popped_character;
}

void clear(StackNode** top) {
	while (*top != NULL) {
		pop(top);
	}
}
