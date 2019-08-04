const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {

    entry : "./portfolio/static/portfolio/styles/index.js",
    output: {
        path: path.resolve("./portfolio/static/webpack_bundles"),
        filename: "[name].bundle.js"
    },

    mode: 'development',

    plugins:
        [new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: "[name].css",
            chunkFilename: "[id].css"
        })
    ],

    module: {
        rules: [{
            test: /\.scss$/,
            use: [
                // fallback to style-loader in development
                // 'style-loader',
                {
                    loader: MiniCssExtractPlugin.loader,
                    options: {
                        // you can specify a publicPath here
                        // by default it uses publicPath in webpackOptions.output
                        publicPath: '../',
                        hmr: process.env.NODE_ENV === 'development',
                    },
                },
                "css-loader", // translates CSS into CommonJS
                "sass-loader" // compiles Sass to CSS, using Node Sass by default
            ]
        }]
    },

};