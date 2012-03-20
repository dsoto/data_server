
// create date ranges from midnight - midnight local time
var now = new Date();
var date_end = new Date(now.getFullYear(), now.getMonth(), now.getDate());
date_end.setDate(date_end.getDate() + 1);
var date_start = new Date(date_end);
date_start.setDate(date_start.getDate() - 1);
console.log(date_start);
// these seem to be actual date objects

// interval ranges
//    0 -  6 hours - every snapshot
//   30 - 12 hours - 30 second interval
//   60 - 24 hours - 60 second interval
//  300 -  5 days  -  5 minute interval
//  900 - 14 days  - 15 minute interval
// 3600 - 31 days  -  1 hour   interval

// pachube url
// the iso dates are on UTC
var url = "http://108.166.92.185:8000?"
        + "date_start=" + d3.time.format.iso(date_start)
        + "&date_end=" + d3.time.format.iso(date_end)
        + "&tag=kitchen";

console.log(url);


jQuery.getJSON(
    url,
    {format:"json"}).done(function (data) {
        //console.log(data);
        var times = new Array();
        var ydata = new Array();
        for (i in data) {
            /*
            document.write(data[i].time_stamp);
            document.write('<br>');
            document.write(data[i].value);
            document.write('<br>');
            */
            //times[i] = data[i].time_stamp;
            ydata[i] = data[i].value;
            times[i] = new Date(data[i].time_stamp);
            data[i].time_stamp = new Date(data[i].time_stamp);
            /*
            data[i].value = data[i].value / 4096.0 * 1.8 * 100;
            // date object


            //data[i].time_stamp = +data[i].time_stamp;

            console.log(data[i].time_stamp);
            */
         }
              //  console.log(ydata);
                //console.log(times);



             var range_round = 1,
             yrange_max = Math.ceil(d3.max(ydata) / range_round) * range_round,
             yrange_min = Math.floor(d3.min(ydata) / range_round) * range_round,
             w = 1000,
             h = 500,
             p = 50,
             x = d3.time.scale()
                        //.domain([d3.min(times),d3.max(times)])
                        .domain([date_start, date_end])
                        //.domain([d3.time.format.iso(date_start), d3.time.format.iso(date_end)])
                        .range([0,w]),
             y = d3.scale.linear()
                         .domain([yrange_min, yrange_max])
                         .range([h,0]);

        console.log(x(date_end))
        for (i in data){
            console.log(times[i]);
            console.log(x(times[i]));
        }


         // create axes
         var vis = d3.select("#graph")
                     .data([data])
                     .append("svg:svg")
                     .attr("width", w + p * 2)
                     .attr("height", h + p * 2)
                     .append("svg:g")
                     .attr("transform", "translate(" + p + "," + p + ")");

         // line path
         vis.append("svg:path")
            .attr("class","line")
            .attr("d", d3.svg.line()
             // d is some magic that iterates over the d3values object
            .x( function(d) { return x(d.time_stamp);} )
            .y( function(d) { return y(d.value);} ));


        // data points as circles
        vis.selectAll("circle.line")
            .data(data)
            .enter().append("svg:circle")
            .attr("class","line")
            .attr("cx", function(d) { return x(d.time_stamp);})
            .attr("cy", function(d) { return y(d.value);})
            .attr("r", 2);

         var vrules = vis.selectAll("g.vrule")
             .data(x.ticks(d3.time.hours, 12))
             .enter().append("svg:g")
             .attr("class", "rule");

         // vertical grid lines
         vrules.append("svg:line")
             //.attr("class", function (d,i) {return i ? null : "axis";})
             .attr("x1", x)
             .attr("x2", x)
             .attr("y1", 0)
             .attr("y2", h - 1);

         // x tick text
         vrules.append("svg:text")
             .attr("x", x)
             .attr("y", h + 20)
             .attr("dy", ".71em")
             .attr("text-anchor", "middle")
             //.text(x.tickFormat(d3.time.hours, 2));
             .text(d3.time.format('%m-%d %H:%M'));

        // vertical axis line
        // right now this is redundant since a line gets inked for each data element
        vrules.append("svg:line")
            // axis has different stroke in css
            .attr("class", "axis")
            .attr("x1", x(d3.min(times)))
            .attr("x2", x(d3.min(times)))
            .attr("y1", y(yrange_min))
            .attr("y2", y(yrange_max));

        var hrules = vis.selectAll("g.hrule")
            .data(y.ticks(10))
            .enter().append("svg:g")
            .attr("class", "rule");

        // y tick text
         hrules.append("svg:text")
             .attr("y", y)
             .attr("x", -10)
             .attr("dy", ".35em")
             .attr("text-anchor", "end")
             .text(y.tickFormat(10));
             //.text(String);

        // horizontal grid lines
         hrules.append("svg:line")
             .attr("x1", x(d3.min(times)))
             .attr("x2", x(d3.max(times)))
             .attr("y1", y)
             .attr("y2", y);

        // horizontal axis line
        hrules.append("svg:line")
            .attr("class", "axis")
            .attr("x1", x(d3.min(times)))
            .attr("x2", x(d3.max(times)))
            .attr("y1", y(yrange_min))
            .attr("y2", y(yrange_min));



/*


    }).fail(function(){
        console.log(this, arguments);
    })
*/
         });
