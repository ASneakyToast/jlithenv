const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry : "./portfolio/static/portfolio/styles/index.js",
    output: {
        path: path.resolve("./portfolio/static/webpack_bundles"),
        filename: "[name].bundle.js"
    },

    mode: 'development',

    module: {
        rules: [{
            test: /\.scss$/,
            use: [
                "style-loader", // creates style nodes from JS strings
                "css-loader", // translates CSS into CommonJS
                "sass-loader" // compiles Sass to CSS, using Node Sass by default
            ]
        }]
    },

    plugins:
        [new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: "[name].css",
            chunkFilename: "[id].css"
        })
    ],

};
//
// let config = {
//
//     // entry: "./portfolio/static/portfolio/styles/index.js",
//
//     output: {
//         path: path.resolve("./portfolio/static/webpack_bundles"),
//         filename: "[name].bundle.js"
//     },
//
//     mode: 'development',
//
//     module: {
//         rules: [
//             {
//                 test: /\.scss$/,
//                 use: [
//                     "style-loader", // creates style nodes from JS strings
//                     "css-loader", // translates CSS into CommonJS
//                     "sass-loader" // compiles Sass to CSS, using Node Sass by default
//                 ]
//             }
//         ]
//     },
//
//     plugins: [
//         new MiniCssExtractPlugin({
//             // Options similar to the same options in webpackOptions.output
//             // both options are optional
//             filename: "[name].css",
//             chunkFilename: "[id].css"
//         })
//     ],
// };
//
// module.export = config;