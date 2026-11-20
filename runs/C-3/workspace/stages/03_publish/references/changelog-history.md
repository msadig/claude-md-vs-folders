# Changelog history (older entries, for reference)

## [2.3.0] - 2026-08-14

### Added
- `Queue.get()` accepts a timeout, thanks @rvdb (#371)
- Worker heartbeats every 10 seconds (#366)

### Fixed
- Jobs scheduled across a DST change ran an hour late (#368)
- `RedisBackend` retried forever on auth errors, thanks @dkowal (#373)

## [2.2.0] - 2026-06-02

### Deprecated
- Positional `ttl` argument on `Queue` (#341)

### Fixed
- Worker crashed on jobs returning generators, thanks @hollis (#344)

## [2.1.0] - 2026-03-20

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [2.0.0] - 2026-01-11

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [1.9.0] - 2025-10-30

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [1.8.0] - 2025-08-01

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

