const { src, dest, watch, series, parallel } = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const cleanCSS = require("gulp-clean-css");
const babel = require("gulp-babel");
const terser = require("gulp-terser");

// RUTAS
const paths = {
    scssAll: "scss/**/*.scss",
    scssNoPartials: ["scss/**/*.scss", "!scss/**/_*.scss"],
    cssOutput: "../app/static/css",
    jsAll: "js/**/*.js",
    jsOutput: "../app/static/js"
}

// COMPILAR Y MINIFICAR SCSS
function styles() {
    return src(paths.scssNoPartials, { base: "scss" })
        .pipe(sass({ quietDeps: true }).on("error", sass.logError))
        .pipe(cleanCSS())
        .pipe(dest(paths.cssOutput));
}

// MINIFICAR JS
function scripts() {
    return src(paths.jsAll, { base: "js" })
        .pipe(babel({ presets: [['@babel/preset-env', { modules: false }]] }))
        .pipe(terser({ module: true }))
        .pipe(dest(paths.jsOutput))
}

// VIGILAR CAMBIOS
function watcher() {
    watch(paths.scssAll, styles);
    watch(paths.jsAll, scripts);
}

// === EXPORTAR TAREAS ===
exports.styles = styles;
exports.scripts = scripts;
exports.default = series(parallel(styles, scripts), watcher);