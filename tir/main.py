from tir.technologies.webapp_internal import WebappInternal
from tir.technologies.apw_internal import ApwInternal

"""
This file must contain the definition of all User Classes.

These classes will contain only calls to the Internal classes.
"""

class Webapp():
    """
    Instantiates the Webapp automated interface testing class.

    :param config_path: The path to the config file. - **Default:** "" (empty string)
    :type config_path: str
    :param autostart: Sets whether TIR should open browser and execute from the start. - **Default:** True
    :type: bool
    """
    def __init__(self, config_path="", autostart=True):
        self.__webapp = WebappInternal(config_path, autostart)
        self.program = ""   # test remarks 26.09 (variable)

    def AddParameter(self, parameter, branch, portuguese_value="", english_value="", spanish_value=""):
        """
        Adds a parameter to the queue of parameters to be set by SetParameters method.

        :param parameter: The parameter name.
        :type parameter: str
        :param branch: The branch to be filled in parameter edit screen.
        :type branch: str
        :param portuguese_value: The value for a portuguese repository.
        :type portuguese_value: str
        :param english_value: The value for an english repository.
        :type english_value: str
        :param spanish_value: The value for a spanish repository.
        :type spanish_value: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.AddParameter("MV_MVCSA1", "", ".F.", ".F.", ".F.")
        """
        self.__webapp.AddParameter(parameter, branch, portuguese_value, english_value, spanish_value)

    def AssertFalse(self):
        """
        Defines that the test case expects a False response to pass

        Usage:

        >>> #Instantiating the class
        >>> inst.oHelper = Webapp()
        >>> #Calling the method
        >>> inst.oHelper.AssertFalse()
        """
        self.__webapp.AssertFalse()

    def AssertTrue(self):
        """
        Defines that the test case expects a True response to pass

        Usage:

        >>> #Instantiating the class
        >>> inst.oHelper = Webapp()
        >>> #Calling the method
        >>> inst.oHelper.AssertTrue()
        """
        self.__webapp.AssertTrue(self.program)

    def ChangeEnvironment(self, date="", group="", branch="", module=""):
        """
        Clicks on the change environment area of Protheus Webapp and
        fills the environment screen.

        :param date: The date to fill on the environment screen. - **Default:** "" (empty string)
        :type date: str
        :param group: The group to fill on the environment screen. - **Default:** "" (empty string)
        :type group: str
        :param branch: The branch to fill on the environment screen. - **Default:** "" (empty string)
        :type branch: str
        :param module: The module to fill on the environment screen. - **Default:** "" (empty string)
        :type module: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.ChangeEnvironment(date="13/11/2018", group="T1", branch="D MG 01 ")
        """
        self.__webapp.ChangeEnvironment(date, group, branch, module)

    def CheckResult(self, field, user_value, grid=False, line=1, grid_number=1, name_attr=False):
        """
        Checks if a field has the value the user expects.

        :param field: The field or label of a field that must be checked.
        :type field: str
        :param user_value: The value that the field is expected to contain.
        :type user_value: str
        :param grid: Boolean if this is a grid field or not. - **Default:** False
        :type grid: bool
        :param line: Grid line that contains the column field to be checked.- **Default:** 1
        :type line: int
        :param grid_number: Grid number of which grid should be checked when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int
        :param name_attr: Boolean if search by Name attribute must be forced. - **Default:** False
        :type name_attr: bool

        Usage:

        >>> # Calling method to check a value of a field:
        >>> oHelper.CheckResult("A1_COD", "000001")
        >>> #-----------------------------------------
        >>> # Calling method to check a field that is on the second line of a grid:
        >>> oHelper.CheckResult("Client", "000001", grid=True, line=2)
        >>> oHelper.LoadGrid()
        >>> #-----------------------------------------
        >>> # Calling method to check a field that is on the second grid of the screen:
        >>> oHelper.CheckResult("Order", "000001", grid=True, line=1, grid_number=2)
        >>> oHelper.LoadGrid()
        """
        self.__webapp.CheckResult(field, user_value, grid, line, grid_number, name_attr)

    def CheckView(self, text, element_type="help"):
        """
        Checks if a certain text is present in the screen at the time and takes an action.

        "help" - closes element.

        :param text: Text to be checked.
        :type text: str
        :param element_type: Type of element. - **Default:** "help"
        :type element_type: str

        Usage:

        >>> # Calling the method.
        >>> oHelper.CheckView("Processing")
        """
        self.__webapp.CheckView(text, element_type)

    def ClickBox(self, fields, contents_list="", select_all=False, grid_number=1):
        """
        Clicks on Checkbox elements of a grid.

        :param field: The column to identify grid rows.
        :type field: str
        :param content_list: Comma divided string with values that must be checked. - **Default:** "" (empty string)
        :type content_list: str
        :param select_all: Boolean if all options should be selected. - **Default:** False
        :type select_all: bool
        :param grid_number: Grid number of which grid should be used when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int
        :param ignore_current: Boolean to ignore the get_current_filtered on loop case of box click. - **Default:** False
        :type ignore_current: bool

        Usage:

        >>> # Calling the method to select a specific checkbox:
        >>> oHelper.ClickBox("Branch", "D MG 01 ")
        >>> #--------------------------------------------------
        >>> # Calling the method to select multiple checkboxes:
        >>> oHelper.ClickBox("Branch", "D MG 01 , D RJ 02")
        >>> #--------------------------------------------------
        >>> # Calling the method to select all checkboxes:
        >>> oHelper.ClickBox("Branch", select_all=True)
        """
        self.__webapp.ClickBox(fields, contents_list, select_all, grid_number)

    def ClickFolder(self, item):
        """
        Clicks on folder elements on the screen.

        :param folder_name: Which folder item should be clicked.
        :type folder_name: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.ClickFolder("Folder1")
        """
        self.__webapp.ClickFolder(item)

    def ClickGridCell(self, column, row=1, grid_number=1):
        """
        Clicks on a Cell of a Grid.

        :param column: The column that should be clicked.
        :type column: str
        :param row_number: Grid line that contains the column field to be checked.- **Default:** 1
        :type row_number: int
        :param grid_number: Grid number of which grid should be checked when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int

        Usage:

        >>> # Calling the method:
        >>> oHelper.ClickGridCell("Product", 1)
        """
        self.__webapp.ClickGridCell(column, row, grid_number)

    def ClickIcon(self, icon_text):
        """
        Clicks on an Icon button based on its tooltip text.

        :param icon_text: The tooltip text.
        :type icon_text: str

        Usage:

        >>> # Call the method:
        >>> oHelper.ClickIcon("Add")
        >>> oHelper.ClickIcon("Edit")
        """
        self.__webapp.ClickIcon(icon_text)

    def ClickCheckBox(self, label_box_name, position=1):
        """
        Clicks on a Label in box on the screen.

        :param label_box_name: The label box name
        :type label_box_name: str
        :param position: index label box on interface
        :type position: int

        Usage:

        >>> # Call the method:
        >>> oHelper.ClickCheckBox("Search",1)
        """
        self.__webapp.ClickCheckBox(label_box_name,position)

    def ClickComboBox(self, position=1, label_comboBox="", flag_cb = False, box_numb = 0):
        """
        Clicks on a Label in box on the screen.

        :param position: Position of text in the combobox, that need to be pressed(will be set)
        :type position: int
        :param label_comboBox: Arguement for detecting combobox by default value in it
        :type label_comboBox: str
        :flag_cb: If set to <True>, then function search specific combobox by xpath on the screen
        :type flag_cb: bool
        :param box_numb: Number of combobox on the screen from <1>
        :type box_numb: int

        Usage:

        >>> # Call the method for one combobox on the screen:
        >>> oHelper.ClickComboBox (position = 2, label_comboBox = "Все блокировки")

        >>> # Call the method for multiple (xpath):
        >>> oHelper.ClickComboBox (position = 2, flag_cb = True, box_numb = 2)
        """
        self.__webapp.ClickComboBox (position, label_comboBox, flag_cb, box_numb)

    def ClickCellGrid(self, xpath_ext):
        """
        Function opens cell in grid, if SetValue(grid=True) doesn't work.
        
        :param xpath_ext: Xpath for unactivated cell
        :type xpath_ext: str

        >>> # Call the method:
        >>> oHelper.ClickCellGrid('//div[contains(@class, "tgetdados twidget dict-msbrgetdbase\")]/div/table/tbody/tr/td[3]')
        >>> oHelper.SetValue('D2_COD', '1016187')
        """
        self.__webapp.ClickCellGrid(xpath_ext)

    def SearchBySearchBox(self, search_txt, search_box_index = 0, filter_index = 0):
        """
        Function searches for data record by selecting between key or column
        
        :param search_txt: String to insert in field to search for recently created data record
        :type search_txt: str
        :param search_box_index: Selecting between type of search (key and column)
        :type search_box_index: int
        :param filter_index: Select search mask
        :type filter_index: int

        >>> # Call the method:
        >>> oHelper.SearchBySearchBox("14/34", 2, 2)
        """
        self.__webapp.SearchBySearchBox(search_txt, search_box_index, filter_index)

    def CheckValuesDB(self, table, field, value, dbg_print=0):
        """
        Function gets value from DB for comparing with recently created value by SetValue() in ma3-GUI testcase

        :param table: Table from DB
        :type table: str
        :param field: Column from DB (in ma3 - field)
        :type field: str
        :param value: Value recently inserted in testcase (for search record in DB column)
        :type value: str
        :param dbg_print: Print in stdout founded record row by value from DB table? (1/0 = Y/N)
        :type dbg_print: int

        Usage:

        >>> # Call the method:
        >>> oHelper.CheckValuesDB(table="sb5000", field="B5_CEME", value='22', dbg_print=1)
        """
        return self.__webapp.CheckValuesDB(table, field, value, dbg_print)

    def ClickLabel(self, label_name):
        """
        Clicks on a Label on the screen.

        :param label_name: The label name
        :type label_name: str

        Usage:

        >>> # Call the method:
        >>> oHelper.ClickLabel("Search")
        """
        self.__webapp.ClickLabel(label_name)

    def GetValue(self, field, grid=False, line=1, grid_number=1):
        """
        Gets the current value or text of element.

        :param field: The field or label of a field that must be checked.
        :type field: str
        :param grid: Boolean if this is a grid field or not. - **Default:** False
        :type grid: bool
        :param line: Grid line that contains the column field to be checked.- **Default:** 1
        :type line: int
        :param grid_number: Grid number of which grid should be checked when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int

        Usage:

        >>> # Calling the method:
        >>> current_value = oHelper.GetValue("A1_COD")
        """
        return self.__webapp.GetValue(field, grid, line, grid_number)

    def LoadGrid(self):
        """
        This method is responsible for running all actions of the input and check queues
        of a grid. After running, the queues would be empty.

        Must be called after SetValue and CheckResult calls that has the grid parameter set to True.

        Usage:

        >>> # After SetValue:
        >>> oHelper.SetValue("A1_COD", "000001", grid=True)
        >>> oHelper.LoadGrid()
        >>> #--------------------------------------
        >>> # After CheckResult:
        >>> oHelper.CheckResult("A1_COD", "000001", grid=True, line=1)
        >>> oHelper.LoadGrid()
        """
        self.__webapp.LoadGrid()

    def LogOff(self):
        """
        Logs out of the Protheus Webapp.
        .. note::
            .Do not use this method in any routine. Use on home screen

        Usage:

        >>> # Calling the method.
        >>> oHelper.LogOff()
        """
        self.__webapp.LogOff()

    def Finish(self):
        """
        Exit the Protheus Webapp.

        Usage:

        >>> # Calling the method.
        >>> oHelper.Finish()
        """
        self.__webapp.Finish()

    def MessageBoxClick(self, button_text):
        """
        Clicks on desired button inside a Messagebox element.

        :param button_text: Desired button to click.
        :type button_text: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.MessageBoxClick("Ok")
        """
        self.__webapp.MessageBoxClick(button_text)

    def Program(self, program_name):
        """
        Method that sets the program in the initial menu search field.

        .. note::
            Only used when the Initial Program is the module Ex: SIGAFAT.

        :param program_name: The program name
        :type program_name: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.Program("MATA020")
        """
        self.program = program_name
        self.__webapp.Program(program_name)

    def RestoreParameters(self):
        """
        Restores parameters to previous value in CFG screen. Should be used after a **SetParameters** call.

        Usage:

        >>> # Adding Parameter:
        >>> oHelper.AddParameter("MV_MVCSA1", "", ".F.", ".F.", ".F.")
        >>> # Calling the method:
        >>> oHelper.SetParameters()
        """
        self.__webapp.RestoreParameters()

    def ScrollGrid(self, column, match_value, grid_number=1):
        """
        Scrolls Grid until a matching column is found.

        :param field: The column to be matched.
        :type field: str
        :param match_value: The value to be matched in defined column.
        :type match_value: str
        :param grid_number: Which grid should be used when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int

        Usage:

        >>> # Calling the method to scroll to a column match:
        >>> oHelper.ScrollGrid(column="Branch",match_value="D MG 01 ")
        >>> #--------------------------------------------------
        >>> # Calling the method to scroll to a column match of the second grid:
        >>> oHelper.ScrollGrid(column="Branch", match_value="D MG 01 ", grid_number=2)
        """
        self.__webapp.ScrollGrid(column, match_value, grid_number)

    def Screenshot(self, filename):
        """
        Takes a screenshot and saves on the screenshot folder defined in config.

        :param filename: The name of the screenshot file.
        :type: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.Screenshot(filename="myscreenshot")
        """
        self.__webapp.take_screenshot(filename)

    def F3(self, field, name_attr=False,send_key=False):
        """
        This method is similar to ClickIcon
        1.Clicks on the Selenium element.

        [Internal]
        Do the standard query(F3) 
        this method 
        1.Search the field
        2.Search icon "lookup"
        3.Click()

        :param term: The term that must be searched.
        :type  term: str
        :param name_attr: True: searchs element by name
        :type  name_attr: bool
        :param send_key: True: try open standard search field send key F3 
        :type bool
        
        Usage:

        >>> # To search using a label name:
        >>> oHelper.F3("Cód")
        >>> #------------------------------------------------------------------------
        >>> # To search using the name of input:
        >>> oHelper.F3(field='A1_EST',name_attr=True)
        >>> #------------------------------------------------------------------------
        >>> # To search using the name of input and do action with a key:
        >>> oHelper.F3(field='A1_EST',name_attr=True,send_key=True)
        """
        self.__webapp.standard_search_field( field, name_attr, send_key )

    def SearchBrowse(self, term, key=None, identifier=None, index=False):
        """
        Searchs a term on Protheus Webapp.

        It will search using the default search key, but if a **key** is provided
        it will search using the chosen key.

        It will search using the first search box on the screen, but if an **identifier**
        is provided, it will search on the chosen search box.

        :param term: The term that must be searched.
        :type term: str
        :param key: The search key to be chosen on the search dropdown. - **Default:** None
        :type key: str
        :param identifier: The identifier of the search box. If none is provided, it defaults to the first of the screen. - **Default:** None
        :type identifier: str
        :param index: Whether the key is an index or not. - **Default:** False
        :type index: bool

        Usage:

        >>> # To search using the first search box and default search key:
        >>> oHelper.SearchBrowse("D MG 001")
        >>> #------------------------------------------------------------------------
        >>> # To search using the first search box and a chosen key:
        >>> oHelper.SearchBrowse("D MG 001", key="Branch+id")
        >>> #------------------------------------------------------------------------
        >>> # To search using a chosen search box and the default search key:
        >>> oHelper.SearchBrowse("D MG 001", identifier="Products")
        >>> #------------------------------------------------------------------------
        >>> # To search using a chosen search box and a chosen search key:
        >>> oHelper.SearchBrowse("D MG 001", key="Branch+id", identifier="Products")
        >>> oHelper.SearchBrowse("D MG 001", identifier="Products")
        >>> #------------------------------------------------------------------------
        >>> # To search using an index instead of name for the search key:
        >>> oHelper.SearchBrowse("D MG 001", key=2, index=True)
        """
        self.__webapp.SearchBrowse(term, key, identifier, index)

    def SetBranch(self, branch):
        """
        Chooses the branch on the branch selection screen.

        :param branch: The branch that would be chosen.
        :type branch: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetBranch("D MG 01 ")
        """
        self.__webapp.SetBranch(branch)

    def Randomex (self, rand_val):
        """
        Method that return random digits of number

        :param rand_val: required number of digits
        :type rand_val: int
        :returns str number

        Usage:

        >>> # Calling the method to get random digits of number to put it in form.
        >>> self.oHelper.SetValue('B1_COD', self.oHelper.Randomex(7))
        """
        return self.__webapp.Randomex (rand_val)

    def FindButton (self, csource, cposition, flag=False):
        """
        Method that gets string label of button from [name_module.tres]
        :param flag: flag that toggles FindButton to search in all tres file [tres25.csv] or in tres folder with all tres's
        :type flag: int
        :param csource: name of the module in lowercase
        :type csource: str
        :param cposition: the [STRxxxx] of the button from [name_module.tres]
        :type cposition: str
        
        Usage:
        >>> # Calling the method to get string label of button, that may be changed for old_test <-> new_translation:
        >>> oHelper.FindButton(csource='mata010', cposition='STR0005')
        """
        return self.__webapp.FindButton (csource, cposition, flag)

    def SetDial (self, head_node, end_index, start_index = 0, attr_name="", attr_contains=""):
        """
        Method that clicks on a scale on the screen.
        :param head_node: Tag container for searching out the elements.
        :type head_node: str
        :param end_index:  - a finite number of fragments of the scale to fill
        :type end_index: int
        :param start_index: Starting index of the first element. - **Default:** 0
        :type start_index: int
        :param attr_name: Unique attribute name to search all scale indices- **Default:** "" (empty string)
        :type attr_name: str
        :param attr_contains: Contents of the unique attribute, of all scale indices- **Default:** "" (empty string)
        :type attr_contains: str

        Usage:
        >>> # Calling the method to click on scale/dial:
        >>> # oHelper.SetDial (head_node="td", end_index = 23, start_index = 0, attr_name="class", attr_contains="worktime-block")
        """
        self.__webapp.SetDial (head_node, end_index, start_index, attr_name, attr_contains)

    def GetModuleName (self, search_function):
        """
        Method that load lines from xlsx(MS Excell) file, and return the module name (SIGAPCP) by function (MATA632).

        :param search_function: Name of routine to search their module.
        :type search_function: str

        Dependencies:
        >>> (lib)Pandas, (file)MODULE_NAME.xlsx

        Usage:

        >>> # Calling the method to search module name by routine name:
        >>> oHelper.Setup(inst.oHelper.GetModuleName("MATA632"), '09/09/2019', '00', '102030', '01')
        """
        return self.__webapp.GetModuleName (search_function)

    def ClickEditButton (self):
        """
        Method selects correct button before checking result with <def CheckResult(), def AssertTrue()>

        Usage:

        >>> # Calling the method to click on a specific button:
        >>> oHelper.ClickEditButton()
        """
        self.__webapp.ClickEditButton()
        
    def SetButton(self, button, sub_item="", position=1, check_error=True):
        """
        Method that clicks on a button on the screen.
        :param button: Button to be clicked.
        :type button: str
        :param sub_item: Sub item to be clicked inside the first button. - **Default:** "" (empty string)
        :type sub_item: str
        :param position: Position which element is located. - **Default:** 1
        :type position: int

        Usage:

        >>> # Calling the method to click on a regular button:
        >>> oHelper.SetButton("Add")
        >>> #-------------------------------------------------
        >>> # Calling the method to click on a sub item inside a button.
        >>> oHelper.SetButton("Other Actions", "Process")
        """
        self.__webapp.SetButton(button, sub_item, position, check_error=check_error)

    def SetFilePath(self, value):
        """
        Fills the path screen with desired path.

        :param value: Path to be inputted.
        :type value: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetFilePath(r"C:\\folder")
        """
        self.__webapp.SetFilePath(value)

    def SetFocus(self, field, grid_cell=False, row_number=1):
        """
        Sets the current focus on the desired field.

        :param field: The field that must receive the focus.
        :type field: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetFocus("A1_COD")
        """
        self.__webapp.SetFocus(field,grid_cell,row_number)

    def SetKey(self, key, grid=False, grid_number=1,additional_key=""): 
        """
        Press the desired key on the keyboard on the focused element.

        Supported keys: F1 to F12, CTRL+Key, ALT+Key, Up, Down, Left, Right, ESC, Enter and Delete

        :param key: Key that would be pressed
        :type key: str
        :param grid: Boolean if action must be applied on a grid. (Usually with DOWN key)
        :type grid: bool
        :param grid_number: Grid number of which grid should be used when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int
		:param additional_key: Key additional that would be pressed.
        :type additional_key: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetKey("ENTER")
        >>> #--------------------------------------
        >>> # Calling the method on a grid:
        >>> oHelper.SetKey("DOWN", grid=True)
        >>> #--------------------------------------
        >>> # Calling the method on the second grid on the screen:
        >>> oHelper.SetKey("DOWN", grid=True, grid_number=2)
        """
        self.__webapp.SetKey(key, grid, grid_number,additional_key)

    def SetLateralMenu(self, menuitens):
        """
        Navigates through the lateral menu using provided menu path.
        e.g. "MenuItem1 > MenuItem2 > MenuItem3"

        :param menu_itens: String with the path to the menu.
        :type menu_itens: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetLateralMenu("Updates > Registers > Products > Groups")
        """
        self.__webapp.SetLateralMenu(menuitens)

    def SetParameters(self):
        """
        Sets the parameters in CFG screen. The parameters must be passed with calls for **AddParameter** method.

        Usage:

        >>> # Adding Parameter:
        >>> oHelper.AddParameter("MV_MVCSA1", "", ".F.", ".F.", ".F.")
        >>> # Calling the method:
        >>> oHelper.SetParameters()
        """
        self.__webapp.SetParameters()

    def SetTabEDAPP(self, table_name):
        """
        Chooses the table on the generic query (EDAPP).

        :param table: The table that would be chosen.
        :type table: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetTabEDAPP("AAB")
        """
        self.__webapp.SetTabEDAPP(table_name)

    def SetValue(self, field, value, grid=False, grid_number=1, ignore_case=True, row=None, name_attr=False, position = 1):
        """
        Sets value of an input element.

        .. note::
            Attention don't use  position parameter with  grid parameter True.

        :param field: The field name or label to receive the value
        :type field: str
        :param value: The value to be inputted on the element.
        :type value: str
        :param grid: Boolean if this is a grid field or not. - **Default:** False
        :type grid: bool
        :param grid_number: Grid number of which grid should be inputted when there are multiple grids on the same screen. - **Default:** 1
        :type grid_number: int
        :param ignore_case: Boolean if case should be ignored or not. - **Default:** True
        :type ignore_case: bool
        :param row: Row number that will be filled
        :type row: int
        :param name_attr: Boolean if search by Name attribute must be forced. - **Default:** False
        :type name_attr: bool
        :param position: Position which element is located. - **Default:** 1
        :type position: int

        Usage:

        >>> # Calling method to input value on a field:
        >>> oHelper.SetValue("A1_COD", "000001")
        >>> #-----------------------------------------
        >>> # Calling method to input value on a field using by label name:
        >>> oHelper.SetValue("Codigo", "000001")
        >>> #-----------------------------------------
        >>> # Calling method to input value on a field using by an existing label name:
        >>> oHelper.SetValue(field = "Codigo", value = "000002", position = 2)
        >>> #-----------------------------------------
        >>> # Calling method to input value on a field that is a grid:
        >>> oHelper.SetValue("Client", "000001", grid=True)
        >>> oHelper.LoadGrid()
        >>> #-----------------------------------------
        >>> # Calling method to checkbox value on a field that is a grid:
        >>> oHelper.SetValue('Confirmado?', True, grid=True)
        >>> oHelper.LoadGrid() 
        >>> #-----------------------------------------
        >>> # Calling method to input value on a field that is on the second grid of the screen:
        >>> oHelper.SetValue("Order", "000001", grid=True, grid_number=2)
        >>> oHelper.LoadGrid()
        """
        return self.__webapp.SetValue(field, value, grid, grid_number, ignore_case, row, name_attr=name_attr)

    def Setup(self, initial_program,  date="", group="99", branch="01", module=""):
        """
        Prepare the Protheus Webapp for the test case, filling the needed information to access the environment.

        :param initial_program: The initial program to load.
        :type initial_program: str
        :param date: The date to fill on the environment screen. - **Default:** "" (empty string)
        :type date: str
        :param group: The group to fill on the environment screen. - **Default:** "99"
        :type group: str
        :param branch: The branch to fill on the environment screen. - **Default:** "01"
        :type branch: str
        :param module: The module to fill on the environment screen. - **Default:** "" (empty string)
        :type module: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.Setup("SIGAFAT", "18/08/2018", "T1", "D MG 01 ")
        """
        self.__webapp.Setup(initial_program, date, group, branch, module)

    def SetTIRConfig(self, config_name, value):
        """
        Changes a value of a TIR internal config during runtime.

        This could be useful for TestCases that must use a different set of configs
        than the ones defined at **config.json**

        Available configs:

        - Url
        - Environment
        - User
        - Password
        - Language
        - DebugLog
        - TimeOut
        - InitialProgram
        - Routine
        - Date
        - Group
        - Branch
        - Module

        :param config_name: The config to be changed.
        :type config_name: str
        :param value: The value that would be set.
        :type value: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.SetTIRConfig(config_name="date", value="30/10/2018")
        """
        self.__webapp.SetTIRConfig(config_name, value)

    def Start(self):
        """
        Opens the browser maximized and goes to defined URL.

        Usage:

        >>> # Calling the method:
        >>> oHelper.Start()
        """
        self.__webapp.Start()

    def TearDown(self):
        """
        Closes the webdriver and ends the test case.

        Usage:

        >>> #Calling the method
        >>> inst.oHelper.TearDown()
        """
        self.__webapp.TearDown()

    def WaitFieldValue(self, field, expected_value):
        """
        Wait until field has expected value.
        Recommended for Trigger fields.

        :param field: The desired field.
        :type field: str
        :param expected_value: The expected value.
        :type expected_value: str

        Usage:

        >>> # Calling method:
        >>> self.WaitFieldValue("CN0_DESCRI", "MY DESCRIPTION")
        """
        self.__webapp.WaitFieldValue(field, expected_value)

    def WaitHide(self, string):
        """
        Search string that was sent and wait hide the elements.

        :param itens: String that will hold the wait.
        :type string: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.WaitHide("Processing")
        """
        self.__webapp.WaitHide(string)

    def WaitProcessing(self, string):
        """
        Uses WaitShow and WaitHide to Wait a Processing screen

        :param string: String that will hold the wait.
        :type string: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.WaitProcessing("Processing")
        """
        self.__webapp.WaitProcessing(string)

    def WaitShow(self, string):
        """
        Search string that was sent and wait show the elements.

        :param itens: String that will hold the wait.
        :type string: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.WaitShow("Processing")
        """
        self.__webapp.WaitShow(string)

    def ClickTree(self, treepath, right_click=False):
        """
        Clicks on TreeView component.

        :param treepath: String that contains the access path for the item separate by ">" .
        :type string: str
        :param right_click: Clicks with the right button of the mouse in the last element of the tree.
        :type string: bool

        Usage:

        >>> # Calling the method:
        >>> oHelper.ClickTree("element 1 > element 2 > element 3")
        >>> # Right Click example:
        >>> oHelper.ClickTree("element 1 > element 2 > element 3", right_click=True)
        """ 
        self.__webapp.ClickTree(treepath, right_click)
    
    def GetText(self, string_left="", string_right=""):
        """
        This method returns a string from modal based on the string in the left or right position that you send on parameter.

        If the string_left was filled then the right side content is return.

        If the string_right was filled then the left side content is return.

        If no parameter was filled so the full content is return.

        :param string_left: String of the left side of content.
        :type string_left: str
        :param string_right: String of the right side of content.
        :type string_right: str

        Usage:

        >>> # Calling the method:
        >>> oHelper.GetText(string_left="Left Text", string_right="Right Text")
        >>> oHelper.GetText(string_left="Left Text")
        >>> oHelper.GetText()
        """

        return self.__webapp.GetText(string_left, string_right)
    
    def CheckHelp(self, text, button=""):
        """
        Checks if some help screen is present in the screen at the time and takes an action.

        :param text: Text to be checked.
        :type text: str
        :param button: Button to be clicked.
        :type button: str

        Usage:

        >>> # Calling the method.
        >>> oHelper.CheckHelp("EXISTCLI Problema: Não pode haver mais...", "Fechar")
        """

        return self.__webapp.CheckHelp(text, button)

    def GiveMeAccess (self):
        """
        Call of the function give to your instance (ex. inst_1) which is copy of WebApp class instance (__webapp),
        private methods from WebappInternal class.
        :param self: Instance of Webapp class
        :type self: instance
        """
        x = self.__webapp                       # object model here, x is link to instance
        return x

    def ClickMenuPopUpItem(self, text, right_click=False):
        """
        Clicks on MenuPopUp Item based in a text

        :param text: Text in MenuPopUp to be clicked.
        :type text: str
        :param right_click: Button to be clicked.
        :type button: bool
        Usage:
        >>> # Calling the method.
        >>> oHelper.ClickMenuPopUpItem("Label")
        """
        return self.__webapp.ClickMenuPopUpItem(text, right_click)
        
class Apw():

    def __init__(self, config_path=""):

        self.__Apw = ApwInternal()

    def CheckBrowse(self, valores):

        self.__Apw.CheckBrowse(valores)


    def CheckLink(self, Link):

        self.__Apw.CheckLink(Link)


    def ClickLink(self, Link):

        self.__Apw.ClickLink(Link)

    def ClickMenu(self, caminho):

        self.__Apw.ClickMenu(caminho)


    def CloseAlert(self):

        self.__Apw.CloseAlert()

    def CloseWindow(self):

        self.__Apw.CloseWindow()

    def EndCase(self):

        self.__Apw.EndCase()

    def SetButton(self, button, type=''):

        self.__Apw.SetButton(button, type)

    def SetGrid(self, btnFunc="Incluir"):

        self.__Apw.SetGrid(btnFunc)

    def SelectBrowse(self, valores, opcao='', duplo=True):

        self.__Apw.SelectBrowse(valores, opcao, duplo)

    def Setup(self, lblUser="Usuário", lblPassword="Senha", btnAccess="Acessar Portal"):

        self.__Apw.Setup(lblUser, lblPassword, btnAccess)

    def SwitchModal(self, opcao, frame=''):

        self.__Apw.SwitchModal(opcao, frame)

    def SwitchWindow(self, exit=False):

        self.__Apw.SwitchWindow(exit)

    def SearchValue(self, busca, valor, grid=False, btnOk='ok', btnFind='buscar', searchparam='Pesquisar'):

        self.__Apw.SearchValue(busca, valor, grid, btnOk, btnFind, searchparam)

    def SetValue(self, campo, valor, grid=False, linha=0, chknewline=False, disabled=False):

        self.__Apw.SetValue(campo, valor, grid, linha, chknewline, disabled)

    def WaitModal(self, text, opcao="title"):
        self.__Apw.WaitModal(text, opcao)
