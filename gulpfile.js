var gulp       = require('gulp');
var less       = require('gulp-less');
var watch      = require('gulp-watch');
var plumber    = require('gulp-plumber');
var autoprefixer = require('gulp-autoprefixer');

var paths = {
    watch: [
        'log/static/log/css/*.less',
        'timelog/static/core/css/*.less',
        ],
    style: 'storage/static/core/css/timelog.less',
    base: 'storage/static',
    build: 'storage/static/build'
}


/* Task to compile less */
gulp.task('compile-less', function() {
  gulp.src(paths.style, {base: paths.base})
    .pipe(plumber())
    .pipe(less())
    .pipe(autoprefixer({ browsers: ['last 2 versions'] }))
    .pipe(gulp.dest(paths.build));
});

/* Task to watch less changes */
gulp.task('watch-less', function() {
  gulp.watch(paths.watch,
             ['compile-less']);
});

/* Task when running `gulp` from terminal */
// gulp.task('default', ['compile-less', 'imagemin', 'watch-less']);
gulp.task('default', ['compile-less', 'watch-less']);