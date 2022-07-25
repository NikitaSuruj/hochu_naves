const form = document.forms.calc;

const typeOfFerm = form.typeOfFerm;
const crate = form.crate;
const widthOfCover = form.widthOfCover;
const lengthOfCover = form.lengthOfCover;
const heightOfFarm = form.heightOfFarm;
const stepOfLag = form.stepOfLag;
const heightOfBeam = form.heightOfBeam;
const convexityOfArch = form.convexityOfArch;
const stepOfBeam = form.stepOfBeam;
const stepOfFarm = form.stepOfFarm;
const thicknessOfLag = form.thicknessOfLag;
const thicknessOfEdge = form.thicknessOfEdge;
const thicknessOfFrame = form.thicknessOfFrame;
const sizeOfBeam = form.sizeOfBeam;
const reinforced = form.reinforced;
const material = form.material;
const parameter = form.parameter;
const colorOfCover = form.colorOfCover;
const colorOfConstruction = form.colorOfConstruction;
const paint = form.paint;
const setup = form.setup;

let price = 228;
let discount = 1337;
let total = 2000;


const typeOfFermTD = document.getElementById('typeOfFermTD');
const crateTD = document.getElementById('crateTD');
const widthOfCoverTD = document.getElementById('widthOfCoverTD');
const lengthOfCoverTD = document.getElementById('lengthOfCoverTD');
const heightOfFarmTD = document.getElementById('heightOfFarmTD');
const stepOfLagTD = document.getElementById('stepOfLagTD');
const heightOfBeamTD = document.getElementById('heightOfBeamTD');
const convexityOfArchTD = document.getElementById('convexityOfArchTD');
const stepOfBeamTD = document.getElementById('stepOfBeamTD');
const stepOfFarmTD = document.getElementById('stepOfFarmTD');
const thicknessOfLagTD = document.getElementById('thicknessOfLagTD');
const thicknessOfEdgeTD = document.getElementById('thicknessOfEdgeTD');
const thicknessOfFrameTD = document.getElementById('thicknessOfFrameTD');
const sizeOfBeamTD = document.getElementById('sizeOfBeamTD');
const reinforcedTD = document.getElementById('reinforcedTD');
const materialTD = document.getElementById('materialTD');
const parameterTD = document.getElementById('parameterTD');
const colorOfCoverTD = document.getElementById('colorOfCoverTD');
const colorOfConstructionTD = document.getElementById('colorOfConstructionTD');
const paintTD = document.getElementById('paintTD');
const setupTD = document.getElementById('setupTD');

const priceTD = document.getElementById('priceTD');
const discountTD = document.getElementById('discountTD');
const totalTD = document.getElementById('totalTD');


form.addEventListener('submit', () => {
    for (let i = 0; i < typeOfFerm.length; i++) {
        if (typeOfFerm[i].checked) {
            console.log(typeOfFerm.value);
            typeOfFermTD.textContent = typeOfFerm[i].value;
            break;
        }
    }

    for (let i = 0; i < crate.length; i++) {
        if (crate[i].checked) {
            console.log(crate.value);
            crateTD.textContent = crate[i].value;
            break;
        }
    }

    console.log(widthOfCover.value);
    console.log(lengthOfCover.value);
    console.log(heightOfFarm.value);
    console.log(stepOfLag.value);
    console.log(heightOfBeam.value);
    console.log(convexityOfArch.value);
    console.log(stepOfBeam.value);
    console.log(stepOfFarm.value);
    console.log(thicknessOfLag.value);
    console.log(thicknessOfEdge.value);
    console.log(thicknessOfFrame.value);
    console.log(thicknessOfFrame.value);
    console.log(sizeOfBeam.value);
    console.log(reinforced.value);
    console.log(material.value);
    console.log(parameter.value);
    console.log(colorOfCover.value);
    console.log(colorOfConstruction.value);
    console.log(paint.value);
    console.log(setup.value);

    console.log(price);
    console.log(discount);
    console.log(total);


    widthOfCoverTD.textContent = widthOfCover.value + ' м';
    lengthOfCoverTD.textContent = lengthOfCover.value + '  м';
    heightOfFarmTD.textContent = heightOfFarm.value + ' м';
    stepOfLagTD.textContent = stepOfLag.value + ' м';
    heightOfBeamTD.textContent = heightOfBeam.value + ' мм';
    convexityOfArchTD.textContent = convexityOfArch.value + ' кг/кв.м.';
    stepOfBeamTD.textContent = stepOfBeam.value + ' м';
    stepOfFarmTD.textContent = stepOfFarm.value + ' мм';
    thicknessOfLagTD.textContent = thicknessOfLag.value + ' мм';
    thicknessOfEdgeTD.textContent = thicknessOfEdge.value + ' мм';
    thicknessOfFrameTD.textContent = thicknessOfFrame.value + ' мм';
    sizeOfBeamTD.textContent = sizeOfBeam.value + ' мм';
    reinforcedTD.textContent = reinforced.value;
    materialTD.textContent = material.value;
    parameterTD.textContent = parameter.value + ' кг/м²';
    colorOfCoverTD.textContent = colorOfCover.value;
    colorOfConstructionTD.textContent = colorOfConstruction.value;
    paintTD.textContent = paint.value;
    setupTD.textContent = setup.value;

    priceTD.textContent = price + ' руб.';
    discountTD.textContent = discount + ' руб.';
    totalTD.textContent = total + ' руб.';
});
