"use strict";

var fs = require('fs');

var ImageTracer = require( __dirname + '/imagetracer.js' );

// This example uses https://github.com/arian/pngjs 
// , but other libraries can be used to load an image file to an ImageData object.
var PNGReader = require( __dirname + '/PNGReader.js' );

// Input and output filepaths / URLs
var infilepath = __dirname + (process.argv[2]);
var outfilepath = __dirname + (process.argv[3]);

fs.readFile(
		
	infilepath,
	
	function( err, bytes ){ // fs.readFile callback
		if(err){ console.log(err); throw err; }
	
		var reader = new PNGReader(bytes);
	
		reader.parse( function( err, png ){ // PNGReader callback
			if(err){ console.log(err); throw err; }
			
			// creating an ImageData object
			var myImageData = { width:png.width, height:png.height, data:png.pixels };
			
			// tracing to SVG string
			var options = { scale: 1 }; // options object; option preset string can be used also
			
			var svgstring = ImageTracer.imagedataToSVG( myImageData, 'posterized1' );
			
			// writing to file
			fs.writeFile(
				outfilepath,
				svgstring,
				function(err){ if(err){  throw err; }  }
			);
			
		});// End of reader.parse()
		
	}// End of readFile callback()
	
);// End of fs.readFile()