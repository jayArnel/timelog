var gulp       = require('gulp');
var less       = require('gulp-less');
var watch      = require('gulp-watch');
var plumber    = require('gulp-plumber');
var autoprefixer = require('gulp-autoprefixer');


/* Task to compile less */
gulp.task('compile-less', function() {
  gulp.src(['storage/static/**/less/*.less'])
    .pipe(plumber())
    .pipe(less())
    .pipe(autoprefixer({ browsers: ['last 2 versions'] }))
    .pipe(gulp.dest('storage/static'));
});

/* Task to watch less changes */
gulp.task('watch-less', function() {
  gulp.watch(['log/static/log/css/*.less'],
             ['compile-less']);
});

/* Task when running `gulp` from terminal */
// gulp.task('default', ['compile-less', 'imagemin', 'watch-less']);
gulp.task('default', ['compile-less', 'watch-less']);