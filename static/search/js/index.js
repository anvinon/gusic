var keyupStack = [];
var keyword = document.getElementById('keyword');
keyword.addEventListener('keyup', function () {
  keyupStack.push(1);

  setTimeout(function () {
    keyupStack.pop();
    if (keyupStack.length === 0) {
      var buf = '.*' + this.value.replace(/(.)/g, "$1.*");
      var reg = new RegExp(buf);
      
      var filteredLists = artists.filter(function (d) {
       return reg.test(d);
      });
      createRow(filteredLists);
    }
  }.bind(this), 300);
});

var createRow = function (lists) {
  var list = document.getElementById('list');
  list.textContent = null;
  lists.forEach(function (l) {
    var li = document.createElement('li');
    li.appendChild(document.createTextNode(l));
    list.appendChild(li);
  });
};

createRow(artists);