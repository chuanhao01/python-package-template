# Generate a coverage badge based on output
.PHONY: test-gen-badge
test-gen-badge:
	poetry run coverage-badge -o assets/images/coverage.svg -f

.PHONY: test
test: test-run test-gen-badge
