#!/usr/bin/env node

const fs = require("fs");

function validateFile(path) {
  try {
    const raw = fs.readFileSync(path, "utf8");
    const parsed = JSON.parse(raw);
    return {
      file: path,
      ok: true,
      type: Array.isArray(parsed) ? "array" : typeof parsed,
      bytes: Buffer.byteLength(raw),
    };
  } catch (error) {
    return {
      file: path,
      ok: false,
      error: error.message,
    };
  }
}

const files = process.argv.slice(2);

if (files.length === 0) {
  console.error("Usage: node tools/json_payload_validator.js <file.json> [...]");
  process.exit(2);
}

const results = files.map(validateFile);
console.log(JSON.stringify(results, null, 2));
process.exit(results.every((result) => result.ok) ? 0 : 1);

