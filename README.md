Cat Classifier
==============
This is a tiny experiment to visualize the activations of each unit of a
neural network based image classifier as a graphical plot.

The image classifier in this experiment is based on a deep neural
network that has 3 hidden layers with 10 units each and a single output
layer. The hidden layers use the ReLU activation function and the output
layer uses the sigmoid activation function.

Although the model trained in this experiment works with about 80%
accuracy, that's not the primary concern of this experiment. The primary
concern of this experiment is to visualize the activations in each unit
of a trained model.


Development Setup
-----------------
The development steps here are written for a Linux or Mac system. All
steps mentioned below assume that Python 3 is installed and you are at
the top-level directory of this project.

 1. Enter the following command to create a Python 3 virtual environment
    with `numpy`, `matplotlib` and `h5py`.

        make venv

 2. Enter the following command to enter the virtual environment.

        . venv

 3. Enter the following command to train a model, test it and write the
    model to a file named `model.json`.

        ./model.py

    To alter the learning parameters, look for the `train()` function in
    this file, edit the values of `iterations` and `alpha` variables and
    run this script again.

 4. Classify arbitrary 64x64 PNG images in the [`extra-set`][T3]
    directory with the following command. You can copy any image into
    this directory as long as it is a 64x64 PNG and run the following
    command.

        ./classify.py

 5. To generate graphical plots of the learned model, enter the
    following command.

        ./plotmodel.py

    This generates activation plots for each unit in the neural network.
    This is explained further in the next section.


Activation Plots
----------------
Here are the graphical plots of the activations in each unit in each
layer. Each image is a visualization of what the activations in a
specific unit looks like. For example, the first image for layer 1 is
the visualization of the activations of the first unit in the first
hidden layer.

Each pixel in an image below represents the activation in a specific
unit for the corresponding pixel in the input image. The activation for
each component (red, green and blue) for each pixel in each unit is
computed separately. Then the activations of red, green and blue
components in each pixel is combined and shown as a single pixel in an
image below.

<!-- BEGIN AUTO -->

### Layer 1 Activations
![Layer 1 Unit 01 Activations](plots/l1a01.png)
![Layer 1 Unit 02 Activations](plots/l1a02.png)
![Layer 1 Unit 03 Activations](plots/l1a03.png)
![Layer 1 Unit 04 Activations](plots/l1a04.png)
![Layer 1 Unit 05 Activations](plots/l1a05.png)
![Layer 1 Unit 06 Activations](plots/l1a06.png)
![Layer 1 Unit 07 Activations](plots/l1a07.png)
![Layer 1 Unit 08 Activations](plots/l1a08.png)
![Layer 1 Unit 09 Activations](plots/l1a09.png)
![Layer 1 Unit 10 Activations](plots/l1a10.png)

### Layer 2 Activations
![Layer 2 Unit 01 Activations](plots/l2a01.png)
![Layer 2 Unit 02 Activations](plots/l2a02.png)
![Layer 2 Unit 03 Activations](plots/l2a03.png)
![Layer 2 Unit 04 Activations](plots/l2a04.png)
![Layer 2 Unit 05 Activations](plots/l2a05.png)
![Layer 2 Unit 06 Activations](plots/l2a06.png)
![Layer 2 Unit 07 Activations](plots/l2a07.png)
![Layer 2 Unit 08 Activations](plots/l2a08.png)
![Layer 2 Unit 09 Activations](plots/l2a09.png)
![Layer 2 Unit 10 Activations](plots/l2a10.png)

### Layer 3 Activations
![Layer 3 Unit 01 Activations](plots/l3a01.png)
![Layer 3 Unit 02 Activations](plots/l3a02.png)
![Layer 3 Unit 03 Activations](plots/l3a03.png)
![Layer 3 Unit 04 Activations](plots/l3a04.png)
![Layer 3 Unit 05 Activations](plots/l3a05.png)
![Layer 3 Unit 06 Activations](plots/l3a06.png)
![Layer 3 Unit 07 Activations](plots/l3a07.png)
![Layer 3 Unit 08 Activations](plots/l3a08.png)
![Layer 3 Unit 09 Activations](plots/l3a09.png)
![Layer 3 Unit 10 Activations](plots/l3a10.png)

### Layer 4 Activations
![Layer 4 Unit 01 Activations](plots/l4a01.png)


Training Images
---------------
<table>
<tr>
  <td>

 ![Training Image 0](train-set/000-not.png)
  <td>

 ![Training Image 1](train-set/001-not.png)
  <td>

 ![Training Image 2](train-set/002-cat.png)
  <td>

 ![Training Image 3](train-set/003-not.png)
  <td>

 ![Training Image 4](train-set/004-not.png)
<tr>
  <td>

 ![Training Image 5](train-set/005-not.png)
  <td>

 ![Training Image 6](train-set/006-not.png)
  <td>

 ![Training Image 7](train-set/007-cat.png)
  <td>

 ![Training Image 8](train-set/008-not.png)
  <td>

 ![Training Image 9](train-set/009-not.png)
<tr>
  <td>

 ![Training Image 10](train-set/010-not.png)
  <td>

 ![Training Image 11](train-set/011-cat.png)
  <td>

 ![Training Image 12](train-set/012-not.png)
  <td>

 ![Training Image 13](train-set/013-cat.png)
  <td>

 ![Training Image 14](train-set/014-cat.png)
<tr>
  <td>

 ![Training Image 15](train-set/015-not.png)
  <td>

 ![Training Image 16](train-set/016-not.png)
  <td>

 ![Training Image 17](train-set/017-not.png)
  <td>

 ![Training Image 18](train-set/018-not.png)
  <td>

 ![Training Image 19](train-set/019-cat.png)
<tr>
  <td>

 ![Training Image 20](train-set/020-not.png)
  <td>

 ![Training Image 21](train-set/021-not.png)
  <td>

 ![Training Image 22](train-set/022-not.png)
  <td>

 ![Training Image 23](train-set/023-not.png)
  <td>

 ![Training Image 24](train-set/024-cat.png)
<tr>
  <td>

 ![Training Image 25](train-set/025-cat.png)
  <td>

 ![Training Image 26](train-set/026-not.png)
  <td>

 ![Training Image 27](train-set/027-cat.png)
  <td>

 ![Training Image 28](train-set/028-not.png)
  <td>

 ![Training Image 29](train-set/029-cat.png)
<tr>
  <td>

 ![Training Image 30](train-set/030-not.png)
  <td>

 ![Training Image 31](train-set/031-not.png)
  <td>

 ![Training Image 32](train-set/032-not.png)
  <td>

 ![Training Image 33](train-set/033-not.png)
  <td>

 ![Training Image 34](train-set/034-not.png)
<tr>
  <td>

 ![Training Image 35](train-set/035-not.png)
  <td>

 ![Training Image 36](train-set/036-not.png)
  <td>

 ![Training Image 37](train-set/037-not.png)
  <td>

 ![Training Image 38](train-set/038-cat.png)
  <td>

 ![Training Image 39](train-set/039-not.png)
<tr>
  <td>

 ![Training Image 40](train-set/040-not.png)
  <td>

 ![Training Image 41](train-set/041-cat.png)
  <td>

 ![Training Image 42](train-set/042-cat.png)
  <td>

 ![Training Image 43](train-set/043-not.png)
  <td>

 ![Training Image 44](train-set/044-not.png)
<tr>
  <td>

 ![Training Image 45](train-set/045-not.png)
  <td>

 ![Training Image 46](train-set/046-not.png)
  <td>

 ![Training Image 47](train-set/047-cat.png)
  <td>

 ![Training Image 48](train-set/048-not.png)
  <td>

 ![Training Image 49](train-set/049-not.png)
<tr>
  <td>

 ![Training Image 50](train-set/050-cat.png)
  <td>

 ![Training Image 51](train-set/051-not.png)
  <td>

 ![Training Image 52](train-set/052-not.png)
  <td>

 ![Training Image 53](train-set/053-not.png)
  <td>

 ![Training Image 54](train-set/054-cat.png)
<tr>
  <td>

 ![Training Image 55](train-set/055-not.png)
  <td>

 ![Training Image 56](train-set/056-cat.png)
  <td>

 ![Training Image 57](train-set/057-cat.png)
  <td>

 ![Training Image 58](train-set/058-not.png)
  <td>

 ![Training Image 59](train-set/059-cat.png)
<tr>
  <td>

 ![Training Image 60](train-set/060-cat.png)
  <td>

 ![Training Image 61](train-set/061-cat.png)
  <td>

 ![Training Image 62](train-set/062-not.png)
  <td>

 ![Training Image 63](train-set/063-not.png)
  <td>

 ![Training Image 64](train-set/064-not.png)
<tr>
  <td>

 ![Training Image 65](train-set/065-not.png)
  <td>

 ![Training Image 66](train-set/066-not.png)
  <td>

 ![Training Image 67](train-set/067-not.png)
  <td>

 ![Training Image 68](train-set/068-cat.png)
  <td>

 ![Training Image 69](train-set/069-not.png)
<tr>
  <td>

 ![Training Image 70](train-set/070-not.png)
  <td>

 ![Training Image 71](train-set/071-cat.png)
  <td>

 ![Training Image 72](train-set/072-not.png)
  <td>

 ![Training Image 73](train-set/073-not.png)
  <td>

 ![Training Image 74](train-set/074-not.png)
<tr>
  <td>

 ![Training Image 75](train-set/075-not.png)
  <td>

 ![Training Image 76](train-set/076-not.png)
  <td>

 ![Training Image 77](train-set/077-not.png)
  <td>

 ![Training Image 78](train-set/078-not.png)
  <td>

 ![Training Image 79](train-set/079-not.png)
<tr>
  <td>

 ![Training Image 80](train-set/080-not.png)
  <td>

 ![Training Image 81](train-set/081-not.png)
  <td>

 ![Training Image 82](train-set/082-not.png)
  <td>

 ![Training Image 83](train-set/083-cat.png)
  <td>

 ![Training Image 84](train-set/084-cat.png)
<tr>
  <td>

 ![Training Image 85](train-set/085-not.png)
  <td>

 ![Training Image 86](train-set/086-not.png)
  <td>

 ![Training Image 87](train-set/087-not.png)
  <td>

 ![Training Image 88](train-set/088-cat.png)
  <td>

 ![Training Image 89](train-set/089-not.png)
<tr>
  <td>

 ![Training Image 90](train-set/090-not.png)
  <td>

 ![Training Image 91](train-set/091-not.png)
  <td>

 ![Training Image 92](train-set/092-cat.png)
  <td>

 ![Training Image 93](train-set/093-cat.png)
  <td>

 ![Training Image 94](train-set/094-cat.png)
<tr>
  <td>

 ![Training Image 95](train-set/095-not.png)
  <td>

 ![Training Image 96](train-set/096-not.png)
  <td>

 ![Training Image 97](train-set/097-cat.png)
  <td>

 ![Training Image 98](train-set/098-not.png)
  <td>

 ![Training Image 99](train-set/099-not.png)
<tr>
  <td>

 ![Training Image 100](train-set/100-not.png)
  <td>

 ![Training Image 101](train-set/101-not.png)
  <td>

 ![Training Image 102](train-set/102-cat.png)
  <td>

 ![Training Image 103](train-set/103-not.png)
  <td>

 ![Training Image 104](train-set/104-cat.png)
<tr>
  <td>

 ![Training Image 105](train-set/105-not.png)
  <td>

 ![Training Image 106](train-set/106-cat.png)
  <td>

 ![Training Image 107](train-set/107-cat.png)
  <td>

 ![Training Image 108](train-set/108-cat.png)
  <td>

 ![Training Image 109](train-set/109-cat.png)
<tr>
  <td>

 ![Training Image 110](train-set/110-cat.png)
  <td>

 ![Training Image 111](train-set/111-cat.png)
  <td>

 ![Training Image 112](train-set/112-not.png)
  <td>

 ![Training Image 113](train-set/113-not.png)
  <td>

 ![Training Image 114](train-set/114-not.png)
<tr>
  <td>

 ![Training Image 115](train-set/115-not.png)
  <td>

 ![Training Image 116](train-set/116-not.png)
  <td>

 ![Training Image 117](train-set/117-cat.png)
  <td>

 ![Training Image 118](train-set/118-not.png)
  <td>

 ![Training Image 119](train-set/119-not.png)
<tr>
  <td>

 ![Training Image 120](train-set/120-not.png)
  <td>

 ![Training Image 121](train-set/121-cat.png)
  <td>

 ![Training Image 122](train-set/122-not.png)
  <td>

 ![Training Image 123](train-set/123-not.png)
  <td>

 ![Training Image 124](train-set/124-cat.png)
<tr>
  <td>

 ![Training Image 125](train-set/125-not.png)
  <td>

 ![Training Image 126](train-set/126-cat.png)
  <td>

 ![Training Image 127](train-set/127-not.png)
  <td>

 ![Training Image 128](train-set/128-cat.png)
  <td>

 ![Training Image 129](train-set/129-cat.png)
<tr>
  <td>

 ![Training Image 130](train-set/130-not.png)
  <td>

 ![Training Image 131](train-set/131-not.png)
  <td>

 ![Training Image 132](train-set/132-not.png)
  <td>

 ![Training Image 133](train-set/133-cat.png)
  <td>

 ![Training Image 134](train-set/134-cat.png)
<tr>
  <td>

 ![Training Image 135](train-set/135-cat.png)
  <td>

 ![Training Image 136](train-set/136-cat.png)
  <td>

 ![Training Image 137](train-set/137-cat.png)
  <td>

 ![Training Image 138](train-set/138-not.png)
  <td>

 ![Training Image 139](train-set/139-not.png)
<tr>
  <td>

 ![Training Image 140](train-set/140-not.png)
  <td>

 ![Training Image 141](train-set/141-not.png)
  <td>

 ![Training Image 142](train-set/142-cat.png)
  <td>

 ![Training Image 143](train-set/143-not.png)
  <td>

 ![Training Image 144](train-set/144-cat.png)
<tr>
  <td>

 ![Training Image 145](train-set/145-cat.png)
  <td>

 ![Training Image 146](train-set/146-cat.png)
  <td>

 ![Training Image 147](train-set/147-not.png)
  <td>

 ![Training Image 148](train-set/148-cat.png)
  <td>

 ![Training Image 149](train-set/149-cat.png)
<tr>
  <td>

 ![Training Image 150](train-set/150-not.png)
  <td>

 ![Training Image 151](train-set/151-not.png)
  <td>

 ![Training Image 152](train-set/152-not.png)
  <td>

 ![Training Image 153](train-set/153-cat.png)
  <td>

 ![Training Image 154](train-set/154-not.png)
<tr>
  <td>

 ![Training Image 155](train-set/155-not.png)
  <td>

 ![Training Image 156](train-set/156-cat.png)
  <td>

 ![Training Image 157](train-set/157-not.png)
  <td>

 ![Training Image 158](train-set/158-not.png)
  <td>

 ![Training Image 159](train-set/159-not.png)
<tr>
  <td>

 ![Training Image 160](train-set/160-not.png)
  <td>

 ![Training Image 161](train-set/161-not.png)
  <td>

 ![Training Image 162](train-set/162-cat.png)
  <td>

 ![Training Image 163](train-set/163-not.png)
  <td>

 ![Training Image 164](train-set/164-cat.png)
<tr>
  <td>

 ![Training Image 165](train-set/165-not.png)
  <td>

 ![Training Image 166](train-set/166-cat.png)
  <td>

 ![Training Image 167](train-set/167-not.png)
  <td>

 ![Training Image 168](train-set/168-not.png)
  <td>

 ![Training Image 169](train-set/169-cat.png)
<tr>
  <td>

 ![Training Image 170](train-set/170-cat.png)
  <td>

 ![Training Image 171](train-set/171-cat.png)
  <td>

 ![Training Image 172](train-set/172-not.png)
  <td>

 ![Training Image 173](train-set/173-not.png)
  <td>

 ![Training Image 174](train-set/174-cat.png)
<tr>
  <td>

 ![Training Image 175](train-set/175-cat.png)
  <td>

 ![Training Image 176](train-set/176-not.png)
  <td>

 ![Training Image 177](train-set/177-cat.png)
  <td>

 ![Training Image 178](train-set/178-not.png)
  <td>

 ![Training Image 179](train-set/179-cat.png)
<tr>
  <td>

 ![Training Image 180](train-set/180-not.png)
  <td>

 ![Training Image 181](train-set/181-not.png)
  <td>

 ![Training Image 182](train-set/182-not.png)
  <td>

 ![Training Image 183](train-set/183-not.png)
  <td>

 ![Training Image 184](train-set/184-not.png)
<tr>
  <td>

 ![Training Image 185](train-set/185-cat.png)
  <td>

 ![Training Image 186](train-set/186-not.png)
  <td>

 ![Training Image 187](train-set/187-not.png)
  <td>

 ![Training Image 188](train-set/188-cat.png)
  <td>

 ![Training Image 189](train-set/189-not.png)
<tr>
  <td>

 ![Training Image 190](train-set/190-not.png)
  <td>

 ![Training Image 191](train-set/191-not.png)
  <td>

 ![Training Image 192](train-set/192-cat.png)
  <td>

 ![Training Image 193](train-set/193-not.png)
  <td>

 ![Training Image 194](train-set/194-not.png)
<tr>
  <td>

 ![Training Image 195](train-set/195-not.png)
  <td>

 ![Training Image 196](train-set/196-not.png)
  <td>

 ![Training Image 197](train-set/197-cat.png)
  <td>

 ![Training Image 198](train-set/198-not.png)
  <td>

 ![Training Image 199](train-set/199-not.png)
<tr>
  <td>

 ![Training Image 200](train-set/200-cat.png)
  <td>

 ![Training Image 201](train-set/201-not.png)
  <td>

 ![Training Image 202](train-set/202-not.png)
  <td>

 ![Training Image 203](train-set/203-not.png)
  <td>

 ![Training Image 204](train-set/204-not.png)
<tr>
  <td>

 ![Training Image 205](train-set/205-not.png)
  <td>

 ![Training Image 206](train-set/206-not.png)
  <td>

 ![Training Image 207](train-set/207-not.png)
  <td>

 ![Training Image 208](train-set/208-not.png)
</table>


Test Results
------------
<table>
<tr>
  <td>

  ![Test Image 0](test-set/000-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 1](test-set/001-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 2](test-set/002-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 3](test-set/003-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 4](test-set/004-cat.png)<br>
  <span>not (fail)</span>
<tr>
  <td>

  ![Test Image 5](test-set/005-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 6](test-set/006-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 7](test-set/007-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 8](test-set/008-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 9](test-set/009-cat.png)<br>
  <span>cat (pass)</span>
<tr>
  <td>

  ![Test Image 10](test-set/010-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 11](test-set/011-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 12](test-set/012-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 13](test-set/013-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 14](test-set/014-not.png)<br>
  <span>not (pass)</span>
<tr>
  <td>

  ![Test Image 15](test-set/015-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 16](test-set/016-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 17](test-set/017-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 18](test-set/018-cat.png)<br>
  <span>not (fail)</span>
  <td>

  ![Test Image 19](test-set/019-cat.png)<br>
  <span>not (fail)</span>
<tr>
  <td>

  ![Test Image 20](test-set/020-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 21](test-set/021-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 22](test-set/022-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 23](test-set/023-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 24](test-set/024-cat.png)<br>
  <span>cat (pass)</span>
<tr>
  <td>

  ![Test Image 25](test-set/025-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 26](test-set/026-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 27](test-set/027-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 28](test-set/028-cat.png)<br>
  <span>not (fail)</span>
  <td>

  ![Test Image 29](test-set/029-not.png)<br>
  <span>cat (fail)</span>
<tr>
  <td>

  ![Test Image 30](test-set/030-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 31](test-set/031-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 32](test-set/032-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 33](test-set/033-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 34](test-set/034-not.png)<br>
  <span>not (pass)</span>
<tr>
  <td>

  ![Test Image 35](test-set/035-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 36](test-set/036-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 37](test-set/037-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 38](test-set/038-not.png)<br>
  <span>cat (fail)</span>
  <td>

  ![Test Image 39](test-set/039-not.png)<br>
  <span>not (pass)</span>
<tr>
  <td>

  ![Test Image 40](test-set/040-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 41](test-set/041-cat.png)<br>
  <span>not (fail)</span>
  <td>

  ![Test Image 42](test-set/042-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 43](test-set/043-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 44](test-set/044-not.png)<br>
  <span>cat (fail)</span>
<tr>
  <td>

  ![Test Image 45](test-set/045-not.png)<br>
  <span>not (pass)</span>
  <td>

  ![Test Image 46](test-set/046-cat.png)<br>
  <span>not (fail)</span>
  <td>

  ![Test Image 47](test-set/047-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 48](test-set/048-cat.png)<br>
  <span>cat (pass)</span>
  <td>

  ![Test Image 49](test-set/049-not.png)<br>
  <span>not (pass)</span>
</table>


Test Accuracy
-------------
Out of 50 test samples, 41 were correctly classified.

The test accuracy is: 82.00%.
<!-- END AUTO -->

Alter the learning parameters in `iterations` and `alpha` variables in
`train()` and `backward` functions, respectively, of `model.py` to alter
the test accuracy.


Training and Test Sets
----------------------
The training images and test images are present in [`train-set`][T1] and
[`test-set`][T2] directories.

The training and test data were obtained from a few HDF5 files shared by
Andrew Ng. The original H5 files are present in the [`h5data`][H1]
directory.

The script [`h5toimg.py`][H2] converts this data to separate PNG image
files and writes them to [`train-set`][T1] and [`test-set`][T2]
directories.

[T1]: ./train-set
[T2]: ./test-set
[T3]: ./extra-set
[H1]: ./h5data
[H2]: ./h5toimg.py
