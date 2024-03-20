const pdf = require('pdfkit');
pdf.PDFDocument.prototype._setFillColor = function (color) {
    const components = color.components;
    this._fillColor = this._fillColorSpace === 'gray' ? components[0] : components;
    if (this.page) {
        this.page.write("/" + this.page._dictRef(color));
    }
};