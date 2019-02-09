// queue()
//     .defer(d3.json, "/Alldata")
//     .await(buildPlot);

d3.json("/Alldata", (function (data) {
        console.log(data);
        var ny = crossfilter(data);
        var all = ny.groupAll();
             




var sexTypeDim = ny.dimension(function (d){ return d.Sex; });
var LeadingTypeDim = ny.dimension(function (d){ return d.LeadingCause; });
var YearTypeDim = ny.dimension(function (d){ return d.Year; });
var RaceEthnicityTypeDim = ny.dimension(function (d){ return d.RaceEthnicity; });
var DeathsTypeDim = ny.dimension(function (d){ return d.Deaths; });
// var AgeAdjustedDeathRateTypeDim = ny.dimension(function (d){ return d.AgeAdjustedDeathRate; });




var sexTypeGroup = sexTypeDim.group()
.reduceCount(function(d){return d.Sex;});

var LeadingTypeGroup = LeadingTypeDim.group()
.reduceCount(function(d){return d.LeadingCause;});
    
var YearTypeGroup = YearTypeDim.group()
.reduceCount(function(d){return d.Year;});

var RaceEthnicityTypeGroup = RaceEthnicityTypeDim.group()
.reduceCount(function(d){return d.RaceEthnicity;});

var DeathsTypeGroup = DeathsTypeDim.group()
.reduceCount(function(d){return d.Deaths;});

// var AgeAdjustedDeathRateTypeGroup = AgeAdjustedDeathRateTypeDim.group()
// .reduceCount(function(d){return d.Deaths;});



var LeadingTypeChart = dc.rowChart("#LeadingType");
var SexTypeChart = dc.rowChart("#SexType");
var YearTypeChart = dc.rowChart("#Year");
var RaceEthnicityTypeChart = dc.rowChart("#RaceEthnicity");
var DeathsTypeChart = dc.pieChart("#Deaths");
// var AgeAdjustedDeathRateTypeChart = dc.rowChart("#AgeAdjustedDeathRate");


LeadingTypeChart
        .height(500)
        .dimension(LeadingTypeDim)
        .group(LeadingTypeGroup)
        .elasticX(true)
        .data(function (group){ return group.top(10);});

SexTypeChart
        .dimension(sexTypeDim)
        .group(sexTypeGroup)
        .elasticX(true);

YearTypeChart
        .dimension(YearTypeDim)
        .group(YearTypeGroup)
        .elasticX(true);

RaceEthnicityTypeChart
        .dimension(RaceEthnicityTypeDim)
        .group(RaceEthnicityTypeGroup)
        .elasticX(true);

DeathsTypeChart
        .width(400)
        .height(400)
        .dimension(DeathsTypeGroup)
        .group(RaceEthnicityTypeGroup)
        .radius(200)
        .slicesCap(5)
        .data(function (group){ return group.top(10);});


dc.renderAll();

    }));

// buildCharts();
// }