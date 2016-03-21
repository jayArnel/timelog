var gulp       = require('gulp');
var sass       = require('gulp-sass');
var watch      = require('gulp-watch');
var plumber    = require('gulp-plumber');
var autoprefixer = require('gulp-autoprefixer');

var paths = {
    watch: [
        'log/static/log/css/*.scss',
        'timelog/static/core/css/*.scss',
        ],
    style: 'storage/static/core/css/timelog.scss',
    base: 'storage/static',
    build: 'timelog/static/build'
}


/* Task to build css from scss files */
gulp.task('buildcss', function() {
  gulp.src(paths.style, {base: paths.base})
    .pipe(plumber())
    .pipe(sass())
    .pipe(autoprefixer({ browsers: ['last 2 versions'] }))
    .pipe(gulp.dest(paths.build));
});

/* Task to watch sass changes */
gulp.task('watch', function() {
  gulp.watch(paths.watch,
             ['buildcss']);
});

/* Task when running `gulp` from terminal */
// gulp.task('default', ['compile-less', 'imagemin', 'watch-less']);
// gulp.task('default', ['compile-less', 'watch']);