export class ResultsComponent {
   // Sample scores for questions
  var scores = [5, 7, 4, 8, 6, 9, 2, 3, 7, 6];

  // Question labels
  var questions = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'];

  // Calculate radians for each question
  var radians = d3.scaleLinear()
    .domain([0, questions.length])
    .range([0, 2 * Math.PI]);

  // Create SVG container
  var svg = d3.select("body")
    .append("svg")
    .attr("width", 600)
    .attr("height", 400)
    .append("g")
    .attr("transform", "translate(300,200)");

  // Draw lines and labels for each question
  for (var i = 0; i < questions.length; i++) {
    var angle = radians(i);
    var x1 = Math.cos(angle) * 50;
    var y1 = Math.sin(angle) * 50;
    var x2 = Math.cos(angle) * 150;
    var y2 = Math.sin(angle) * 150;

    // Draw line
    svg.append("line")
      .attr("x1", x1)
      .attr("y1", y1)
      .attr("x2", x2)
      .attr("y2", y2)
      .style("stroke", "blue");

    // Draw label
    svg.append("text")
      .attr("x", x2)
      .attr("y", y2)
      .text(questions[i])
      .attr("dy", "0.35em")
      .attr("text-anchor", function(d) { return angle > Math.PI ? "end" : null; });
  }

  // Draw points for each question with scores
  for (var i = 0; i < questions.length; i++) {
    var angle = radians(i);
    var score = scores[i];
    var x = Math.cos(angle) * (50 + (score * 10)); // Adjust radius based on score
    var y = Math.sin(angle) * (50 + (score * 10)); // Adjust radius based on score

    // Draw point
    svg.append("circle")
      .attr("cx", x)
      .attr("cy", y)
      .attr("r", 5)
      .style("fill", "blue");
  }
  }
  