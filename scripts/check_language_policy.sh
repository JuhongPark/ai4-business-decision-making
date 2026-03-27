#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

approved_legacy_reference_files=(
  "research/extensions/business-alignment/alignment-ecosystem/ai-safety-fellowships-directory.md"
  "research/extensions/business-alignment/alignment-ecosystem/alignment-programs.md"
  "research/extensions/business-alignment/alignment-ecosystem/alignment-codebases.md"
)

disallowed_letter_pattern='(?:(?!\p{Latin})\p{L})'

for file in "${approved_legacy_reference_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing approved legacy reference file: $file" >&2
    exit 1
  fi

  if ! grep -qx 'status: bilingual_reference_note' "$file"; then
    echo "Approved legacy reference file is missing the required status marker: $file" >&2
    exit 1
  fi
done

matches=""

if command -v rg >/dev/null 2>&1; then
  rg_args=(rg -n --hidden --pcre2 --glob '!.git')
  for file in "${approved_legacy_reference_files[@]}"; do
    rg_args+=(--glob "!$file")
  done
  matches="$("${rg_args[@]}" "$disallowed_letter_pattern" . || true)"
else
  while IFS= read -r file; do
    skip_file=0
    for allowed in "${approved_legacy_reference_files[@]}"; do
      if [[ "$file" == "./$allowed" ]]; then
        skip_file=1
        break
      fi
    done

    if [[ "$skip_file" -eq 1 ]]; then
      continue
    fi

    file_matches="$(perl -CS -ne 'while(/(\p{L})/gu){if($1 !~ /\p{Latin}/){print "$ARGV:$.:$_"; last}}' "$file" 2>/dev/null || true)"
    if [[ -n "$file_matches" ]]; then
      matches+="$file_matches"$'\n'
    fi
  done < <(find . -path ./.git -prune -o -type f -print)
fi

if [[ -n "$matches" ]]; then
  echo "Tracked repository content must remain in English." >&2
  echo "This check scans the working tree, so untracked drafts are included." >&2
  echo "Unexpected non-English-script letters were found outside approved legacy reference files:" >&2
  echo "$matches" >&2
  echo >&2
  echo "Approved legacy reference files:" >&2
  printf '  - %s\n' "${approved_legacy_reference_files[@]}" >&2
  exit 1
fi

echo "Language policy check passed."
